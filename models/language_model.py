from loguru import logger
from config.config_manager import ConfigManager
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


class LanguageModel:
    _single_instance = None

    def __new__(cls, *args, **kwargs):
        if cls._single_instance is None:
            cls._single_instance = super().__new__(cls)
        return cls._single_instance

    def __init__(self):
        self.model = ChatOpenAI(model=ConfigManager().get("model"),
                                temperature=ConfigManager().get("temperature"),
                                timeout=ConfigManager().get("timeout"),
                                )

    def prompt(self, question: str, role: str):
        messages = [
            SystemMessage(role),
            HumanMessage(question),
            ]
        logger.info(self.measure_prompt(question))
        try:
            resp = self.model.invoke(messages)
        except Exception as e:
            print(f"Asking the model failed: {e}")
            return None
        return resp

    def prompt_structured(self, question: str, role: str, structure):
        messages = [
            SystemMessage(role),
            HumanMessage(question),
        ]
        logger.info(self.measure_prompt(question))
        structured_model = self.model.with_structured_output(schema=structure)
        try:
            resp = structured_model.invoke(messages)
        except Exception as e:
            print(f"Asking the model failed: {e}")
            return None
        return resp

    def measure_prompt(self, prompt: str):
        return self.model.get_num_tokens(prompt)

