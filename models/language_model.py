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
        print(messages)
        try:
            resp = self.model.invoke(messages)
        except Exception as e:
            print(f"Asking the model failed: {e}")
            return None
        return resp

