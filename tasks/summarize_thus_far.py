from prompts import Prompts
from models.language_model import LanguageModel
from structures.formats.partial_summary import PartialSummary


def summarize_thus_far(previous_summary: str, new_scene_text: str) -> str:
    """Summarize the story thus far with the new scene added"""
    prompt = Prompts().format_prompt("summarize scenes",
                                     partial_summary=previous_summary,
                                     scene=new_scene_text)
    role = """You are a professional writer, a skilled storyteller and master stylist, outlining your new story."""
    result = LanguageModel().prompt_structured(question=prompt,
                                               role=role,
                                               structure=PartialSummary)
    summary = getattr(result, "summary", None)
    if not summary:
        raise ValueError("Failed to summarize the story thus far.")
    return summary
