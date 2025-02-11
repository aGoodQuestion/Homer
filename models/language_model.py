from loguru import logger

from util.singleton_meta import SingletonMeta
from config.config_manager import ConfigManager
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


class LanguageModel(metaclass=SingletonMeta):
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
        logger.debug(f"passing prompt of {self.measure_prompt(messages)} tokens to LLM")
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
        logger.debug(f"passing prompt of {self.measure_prompt(messages)} tokens to LLM")
        structured_model = self.model.with_structured_output(schema=structure)
        try:
            resp = structured_model.invoke(messages)
        except Exception as e:
            print(f"Asking the model failed: {e}")
            return None
        return resp

    def measure_prompt_elements(self, question: str, role: str = ""):
        messages = question + role
        return self.model.get_num_tokens(messages)

    def measure_prompt(self, prompt: list):
        return self.model.get_num_tokens_from_messages(prompt)


