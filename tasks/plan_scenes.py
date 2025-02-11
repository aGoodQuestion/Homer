from structures import Story
from models.language_model import LanguageModel
from prompts import Prompts
from structures.formats.scene_description import SceneDescriptions


def plan_scenes(story: Story) -> list[SceneDescriptions]:
    """Plan the scenes for a story"""
    prompt = Prompts().format_prompt("plan scenes",
                                     title=story.title,
                                     premise=story.premise,
                                     number_of_scenes=story.num_scenes,
                                     character_list=story.character_list_string())
    role = """You are a professional writer, a skilled storyteller and master stylist, planning a new story."""
    result = LanguageModel().prompt_structured(question=prompt,
                                               role=role,
                                               structure=SceneDescriptions)
    scenes = getattr(result, "scenes", [])
    return scenes
