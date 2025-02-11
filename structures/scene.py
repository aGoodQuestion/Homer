from dataclasses import dataclass


@dataclass
class Scene:
    def __init__(self, initial_description: str, characters: str, text: str, summary_through_here: str):
        self.initial_description: str = initial_description
        self.characters: str = characters
        self.text: str = text
        self.summary_through_here: str = summary_through_here