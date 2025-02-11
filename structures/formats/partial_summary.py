from pydantic import BaseModel, Field


class PartialSummary(BaseModel):
    """The summary of the story through a particular scene"""
    summary: str = Field(..., title="Summary", description="The summary of the story through this most recent scene")
