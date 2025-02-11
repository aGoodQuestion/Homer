from typing import List

from pydantic import BaseModel, Field


class SceneDescription(BaseModel):
    """A planned scene for the story"""
    description: str = Field(..., title="Description", description="A brief description of this scene")
    characters: str = Field(..., title="Characters", description="A comma-separated list of just the characters featured in this scene")


class SceneDescriptions(BaseModel):
    """A collection of scenes for the story"""
    scenes: List[SceneDescription] = Field(..., title="Scenes", description="A list of scenes composing the story")
