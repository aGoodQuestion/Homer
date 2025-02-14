from langgraph.graph import StateGraph, START, END
from loguru import logger

from structures import Story
from structures.enums import StatusType
from tasks.plan_scenes import plan_scenes
from tasks.draft_scenes import draft_scenes
from util.status import Status


def plan_story(state: Story):
    logger.debug("--Plan Story Node--")
    Status().update(StatusType.MESSAGE, f"Planning {state.num_scenes} scenes for {state.title}...")
    scene_list = plan_scenes(state)
    if not scene_list or len(scene_list) != state.num_scenes:
        Status().update(StatusType.CONCLUDE_FAILURE, "Scene planning failed, story writing terminated.")
        # return None
    Status().update(StatusType.MESSAGE, f"...{state.num_scenes} planned.")
    return {"scene_descriptions": scene_list}


def draft_story(state: Story):
    logger.debug("--Draft Story Node--")
    Status().update(StatusType.MESSAGE, "Putting together a first draft scene-by-scene...")
    scenes = draft_scenes(state)
    if not scenes or len(scenes) != state.num_scenes:
        Status().update(StatusType.CONCLUDE_FAILURE, "Scene drafting failed, story writing terminated.")
        # return None
    Status().update(StatusType.MESSAGE, "...first draft of all scenes complete.")
    return {"scenes": scenes}


builder = StateGraph(Story)
builder.add_node("plan_story", plan_story)
builder.add_node("draft_story", draft_story)
builder.add_edge(START, "plan_story")
builder.add_edge("plan_story", "draft_story")
builder.add_edge("draft_story", END)


graph = builder.compile()


def write_story(the_story: Story):
    graph_result = graph.invoke(the_story)
    return graph_result
