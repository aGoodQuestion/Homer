from loguru import logger
from dataclasses import dataclass, field

from structures.character import Character
from structures.formats import SceneDescription
from structures.scene import Scene


@dataclass
class Story:
    title: str
    premise: str
    num_scenes: int
    characters: list[Character]
    scene_descriptions: list[SceneDescription] = field(default_factory=list)
    scenes: list[Scene] = field(default_factory=list)

    # def __init__(self, title: str, premise: str, num_scenes: int, characters: list[Character]):
    #     self.title = title
    #     self.premise = premise
    #     self.num_scenes = num_scenes
    #     self.characters = characters
    #     self.scenes_descriptions = list()
    #     self.scenes = list()

    def character_list_string(self) -> str:
        string = ""
        for i, character in enumerate(self.characters):
            string += f"{i+1}. {character.name} - {character.description}\n"
        return string

    def selective_character_list_string(self, characters_to_include: str) -> str:
        character_list = [x.strip() for x in characters_to_include.split(",")]
        string = ""
        for i, character in enumerate(self.characters):
            if character.name in character_list:
                string += f"{i+1}. {character.name} - {character.description}\n"
                character_list.remove(character.name)
        if character_list:
            logger.warning(f"Characters not found: {character_list}")
        return string
