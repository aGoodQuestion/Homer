from pathlib import Path
from langchain_core.prompts import PromptTemplate


class Prompts:
    _single_instance = None

    def __new__(cls, *args, **kwargs):
        if cls._single_instance is None:
            cls._single_instance = super().__new__(cls)
        return cls._single_instance

    def __init__(self):
        pt_path = self.prompt_templates_path = Path(__file__).resolve().parent / 'prompt_templates'
        if not pt_path.exists():
            raise ValueError(f"Prompt templates not found at {pt_path}.")
        self.prompt_templates = {}

        for template_file in pt_path.rglob('*.prompt'):
            self.prompt_templates[template_file.stem] = self._load_text_as_pt(template_file)

    def _load_text_as_pt(self, template_file: Path):
        with open(template_file, 'r') as f:
            return PromptTemplate.from_template(f.read())

    def get_template(self, name: str):
        if name in self.prompt_templates:
            return self.prompt_templates[name]
        else:
            raise ValueError(f"Prompt template '{name}' not found.")

    def format_prompt(self, name: str, **kwargs):
        return self.get_template(name).format(**kwargs)
