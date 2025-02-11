from pydantic import BaseModel, Field


class SceneDraft(BaseModel):
    """The text of scene in a story"""
    text: str = Field(..., title="Text", description="The full, polished text of a particular scene in a compelling story")
