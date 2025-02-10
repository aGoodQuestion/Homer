from typing import List

from pydantic import BaseModel, Field


class Scene(BaseModel):
    """A planned scene for the story"""
    description: str = Field(..., title="Description", description="A brief description of this scene")
    characters: str = Field(..., title="Characters", description="A list of just the characters featured in this scene")


class Scenes(BaseModel):
    """A collection of scenes for the story"""
    scenes: List[Scene] = Field(..., title="Scenes", description="A list of scenes composing the story")
