from pydantic import BaseModel, Field


class ConsistencyCritique(BaseModel):
    """A critique of a story scene based on whether it is consistent with its characters and the scenes prior"""
    character_issues: str = Field(..., title="Character Issues", description="Any issues relating to characters in the scene that are inconsistent with their established personality, motives, etc. (if applicable, if there are no contradictions, simply put 'None')")
    plot_issues: str = Field(..., title="Plot Issues", description="Any issues relating to events or details in the scene which are inconsistent with those depicted in the scene prior (If applicable, if there are no contradictions, simply put 'None')")