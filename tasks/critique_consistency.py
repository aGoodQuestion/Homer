from loguru import logger

from structures.formats.consistency_critique import ConsistencyCritique
from structures.story import Story
from util.status import Status
from structures.enums import StatusType
from models.language_model import LanguageModel
from prompts import Prompts


def critique_scene_consistency(scene_text: str, scene_prior: str, character_list: str) -> ConsistencyCritique:
    prompt = Prompts().format_prompt("critique consistency",
                                     scene=scene_text,
                                     prior_scene=scene_prior,
                                     character_descriptions=character_list)
    role = "You are a perceptive reader, analyzing a story for internal consistency."
    result = LanguageModel().prompt_structured(question=prompt,
                                               role=role,
                                               structure=ConsistencyCritique)
    return result


def critique_consistency(story: Story) -> dict:
    """Provide a consistency critique of each scene in the story"""
    critiques = {}
    for i in range(story.num_scenes):
        Status().update(type=StatusType.MESSAGE,
                        message=f"Critiquing scene {i + 1} for consistency...",
                        tabs=1)
        result = critique_scene_consistency(scene_text=story.scenes[i].text,
                                            scene_prior=story.scenes[i-1].text if i > 0 else "[There is no prior scene as the scene you're critiqueing begins the story.]",
                                            character_list=story.selective_character_list_string(story.scenes[i].characters))
        logger.debug(f"Initial critique for scene {i}: {result}")
        critiques[i] = []
        if result.plot_issues.lower() != "none":
            critiques[i].append(result.plot_issues)
        if result.character_issues.lower() != "none":
            critiques[i].append(result.character_issues)
        Status().update(type=StatusType.MESSAGE,
                        message=f"...scene {i + 1} critiqued.",
                        tabs=1)
    return critiques
