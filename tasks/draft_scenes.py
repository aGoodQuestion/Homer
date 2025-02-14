from structures import Story, Scene
from structures.formats import SceneDraft
from structures.enums import StatusType
from models.language_model import LanguageModel
from prompts import Prompts
from tasks.summarize_thus_far import summarize_thus_far
from util.status import Status


def draft_scene(scene_description: str, character_list: str, summary_prior: str) -> str:
    prompt = Prompts().format_prompt("draft scene",
                                     character_list=character_list,
                                     summary=summary_prior,
                                     scene=scene_description)
    role = """You are a professional writer, a skilled storyteller and master stylist, drafting a new scene for a story."""
    result = LanguageModel().prompt_structured(question=prompt,
                                               role=role,
                                               structure=SceneDraft)
    scene_text = getattr(result, "text", None)
    if not scene_text:
        raise ValueError("Failed to draft the scene.")
    return scene_text


def draft_scenes(story: Story) -> list[Scene]:
    drafted_scenes = []
    for i in range(story.num_scenes):
        Status().update(type=StatusType.MESSAGE,
                        message=f"Drafting scene {i + 1}...",
                        tabs=1)
        scene_description = story.scene_descriptions[i]
        if i == 0:
            summary_prior = "[This is the first scene in the story so nothing has happened yet.]"
        else:
            Status().update(type=StatusType.MESSAGE,
                            message=f"...summarizing the story thus far...",
                            tabs=2)
            summary_prior = drafted_scenes[i-1].summary_through_here
        Status().update(type=StatusType.MESSAGE,
                        message=f"...drafting scene {i + 1} text...",
                        tabs=2)
        scene_text = draft_scene(scene_description=scene_description.description,
                                 character_list=story.selective_character_list_string(scene_description.characters),
                                 summary_prior=summary_prior)
        scene = Scene(initial_description=scene_description.description,
                      characters=scene_description.characters,
                      text=scene_text,
                      summary_through_here=summarize_thus_far(summary_prior, scene_text))
        drafted_scenes.append(scene)
        Status().update(type=StatusType.MESSAGE,
                        message=f'...scene {i + 1} drafted."',
                        tabs=1)
    return drafted_scenes





