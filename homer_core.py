from dotenv import load_dotenv
from loguru import logger

from structures import Story, Character
from tasks.plan_scenes import plan_scenes
from tasks.draft_scenes import draft_scenes


premise = """In the ruins of civilization, after the apocalypse, three friends gather for a picnic."""
characters = [Character(name="Glory", description="""A young woman who had her 18th birthday on the day the world ended
              and is inexplicably cheerful despite the dire circumstances."""),
              Character(name="Cecil", description="""A middle-aged man who was cinical before, and seems faintly amused 
              by what has transpired, as if he always saw it coming. But, deep down, he is terrified of death."""),
              Character(name="Gabriel", description="""Glory's older brother, and long time friend of Cecil. He is 
              determined that he and his will live through this, and into a new world, though no hope of such is 
              forthcoming, and he knows it.""")]
the_story = Story(title="Tea in the Ruin",
                  premise=premise,
                  num_scenes=3,
                  characters=characters)


def main():
    load_dotenv()

    scene_list = plan_scenes(the_story)
    if not scene_list:
        logger.error("Scene planning failed, story writing terminated.")
        return
    the_story.scenes_descriptions = scene_list

    scenes = draft_scenes(the_story)
    if not scenes:
        logger.error("Scene drafting failed, story writing terminated.")
        return
    the_story.scenes = scenes

    the_story.display()




main()
