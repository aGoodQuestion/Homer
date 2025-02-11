from structures import Story
from structures.enums import StatusType
from tasks.plan_scenes import plan_scenes
from tasks.draft_scenes import draft_scenes
from util.status import Status


def write_story(the_story: Story) -> Story | None:
    Status().update(StatusType.MESSAGE, f"Planning {the_story.num_scenes} scenes for {the_story.title}...")
    scene_list = plan_scenes(the_story)
    if not scene_list or len(scene_list) != the_story.num_scenes:
        Status().update(StatusType.CONCLUDE_FAILURE, "Scene planning failed, story writing terminated.")
        return None
    the_story.scenes_descriptions = scene_list
    Status().update(StatusType.MESSAGE, f"...{the_story.num_scenes} planned.")

    Status().update(StatusType.MESSAGE, "Putting together a first draft scene-by-scene...")
    scenes = draft_scenes(the_story)
    if not scenes or len(scenes) != the_story.num_scenes:
        Status().update(StatusType.CONCLUDE_FAILURE, "Scene drafting failed, story writing terminated.")
        return None
    the_story.scenes = scenes
    Status().update(StatusType.MESSAGE, "...first draft of all scenes complete.")

    return the_story
