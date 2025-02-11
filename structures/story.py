from loguru import logger

from structures import Character


class Story:
    def __init__(self, title: str, premise: str, num_scenes: int, characters: list[Character]):
        self.title = title
        self.premise = premise
        self.num_scenes = num_scenes
        self.characters = characters
        self.scenes_descriptions = list()
        self.scenes = list()

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


    def display(self):
        logger.success(f"Title: {self.title}")
        logger.success(f"Premise: {self.premise}")
        logger.success(f"Number of scenes: {self.num_scenes}")
        logger.success("Scenes:")
        for scene in self.scenes:
            logger.info(f"Summary through this scene: {scene.summary_through_here}")
            logger.success("The scene text itself:")
            logger.info(scene.text)
