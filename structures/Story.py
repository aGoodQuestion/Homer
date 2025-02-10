from structures.Character import Character

class Story:
    def __init__(self, title: str, premise: str, num_scenes: int, characters: list[Character]):
        self.title = title
        self.premise = premise
        self.num_scenes = num_scenes
        self.characters = characters
        self.scenes = list()

    def character_list_string(self):
        str = ""
        for i, character in enumerate(self.characters):
            str += f"{i+1}. {character.name} - {character.description}\n"