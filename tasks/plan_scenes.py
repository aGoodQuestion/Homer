from loguru import logger

from structures import Story
from models.language_model import LanguageModel
from prompts.prompts import Prompts
from structures.formats.scenes import Scenes


def plan_scenes(story: Story):
    """Plan the scenes for a story"""
    prompt = Prompts().format_prompt("plan scenes",
                                     title=story.title,
                                     premise=story.premise,
                                     number_of_scenes=story.num_scenes,
                                     character_list=story.character_list_string())
    logger.info(f"Prompt contains {LanguageModel().measure_prompt(prompt)} tokens.")
    role = """You are a professional writer, a skilled storyteller and master stylist, planning a new story."""
    result = LanguageModel().prompt_structured(question=prompt,
                                               role=role,
                                               structure=Scenes)

    return getattr(result, "scenes", None)