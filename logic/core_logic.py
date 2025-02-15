from langgraph.graph import StateGraph, START, END
from loguru import logger

from structures import Story
from structures.enums import StatusType
from tasks.plan_scenes import plan_scenes
from tasks.draft_scenes import draft_scenes
from tasks.critique_consistency import critique_consistency
from util.status import Status


def plan_story(state: Story):
    logger.debug("--Plan Story Node--")
    Status().update(StatusType.MESSAGE, f"Planning {state.num_scenes} scenes for {state.title}...")
    scene_list = plan_scenes(state)
    if not scene_list or len(scene_list) != state.num_scenes:
        return {"errors": state.errors + ["Failed to generate a scene list."]}
    Status().update(StatusType.MESSAGE, f"...{state.num_scenes} planned.")
    return {"scene_descriptions": scene_list}


def post_planning_edge(state: Story):
    logger.debug("--Post Planning Edge--")
    if state.errors:
        Status().update(StatusType.CONCLUDE_FAILURE, "Scene planning failed, story writing terminated.")
        return END
    return "draft_story"


def draft_story(state: Story):
    logger.debug("--Draft Story Node--")
    Status().update(StatusType.MESSAGE, "Putting together a first draft scene-by-scene...")
    scenes = draft_scenes(state)
    if not scenes or len(scenes) != state.num_scenes:
        return {"errors": state.errors + ["Failed to generate a scene list."]}
    Status().update(StatusType.MESSAGE, "...first draft of all scenes complete.")
    return {"scenes": scenes}


def post_drafting_edge(state: Story):
    logger.debug("--Post Drafting Edge--")
    if state.errors:
        Status().update(StatusType.CONCLUDE_FAILURE, "Scene drafting failed, story writing terminated.")
        return END
    return "critique_story_consistency"


def critique_story_consistency(state: Story):
    logger.debug("--Critique Story Consistency Node--")
    Status().update(StatusType.MESSAGE, "Critiquing the story for internal consistency...")
    critiques = critique_consistency(state)
    Status().update(StatusType.MESSAGE, "...story consistency critiqued.")
    for key, value in critiques.items():
        logger.debug(f"Critique for scene {key}: {value}")
    return {"critiques": {key: value + critiques[key] for key, value in state.critiques.items()}}


builder = StateGraph(Story)
builder.add_node("plan_story", plan_story)
builder.add_node("draft_story", draft_story)
builder.add_node("critique_story_consistency", critique_story_consistency)
builder.add_edge(START, "plan_story")
builder.add_edge("critique_story_consistency", END)
builder.add_conditional_edges("plan_story", post_planning_edge)
builder.add_conditional_edges("draft_story", post_drafting_edge)
graph = builder.compile()


def write_story(the_story: Story):
    graph_result = graph.invoke(the_story)
    return graph_result
