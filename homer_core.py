from dotenv import load_dotenv

from structures.Story import Story
from structures.Character import Character
from tasks.plan_scenes import plan_scenes

premise = """In the ruins of civilization, after the apocalypse, three friends gather for a picnic."""
characters = [Character(name="Alice", description="""A young woman who had her 18th birthday on the day the world ended
              and is inexplicably cheerful deespite the dire circumstances."""),
              Character(name="Cecil", description="""A middle-aged man who was cinical before, and seems faintly amused 
              by what has transpired, as if he always saw it coming. But, deep down, he is terrified of death."""),
              Character(name="Gabriel", description="""Alice's older brother, and long time friend of Cecil. He is 
              determined that he and his will live through this, and into a new world, though no hope of such is 
              forthcoming, and he knows it.""")]
the_story = Story(title="Dinner in the Ruin",
                  premise=premise,
                  num_scenes=5,
                  characters=characters)


def main():
    load_dotenv()
    scene_list = plan_scenes(the_story)

    if scene_list:
        for scene in scene_list:
            print(scene.description)
            print(scene.characters)
            print("-" * 80)
    else:
        print("Something went wrong, no scenes planned.")



main()
