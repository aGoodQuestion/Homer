import streamlit as st

from structures import Story, Character


st.set_page_config(
    layout="wide",
    page_title="Homer the Storyteller",
    page_icon="🍩",
)


def draw_character_input(index: int):
    places = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    st.text_input(label=f"Name of the {places[index]} character:",
                  key=f"char_{index}_name",
                  max_chars=100,)
    st.text_area(label=f"Describe the {places[index]} character:",
                 height=140,
                 key=f"char_{index}_description",
                 max_chars=500,
                 )


def initialize_story() -> bool:
    title = st.session_state.get("title")
    premise = st.session_state.get("premise")
    num_scenes = st.session_state.get("num_scenes")
    characters = []
    for i in range(st.session_state.get("num_characters")):
        name = st.session_state.get(f"char_{i}_name")
        description = st.session_state.get(f"char_{i}_description")
        if name and description:
            characters.append(Character(name=name, description=description))
        else:
            return False
    if title and premise and num_scenes and characters:
        st.session_state["the_story"] = Story(title=title,
                                              premise=premise,
                                              num_scenes=num_scenes,
                                              characters=characters)
        return True
    return False


def main():
    st.header("Homer the Storyteller")
    intro_copy = """Welcome to Homer the Storyteller, a tool to help you write stories. Describe the story you want to 
    tell and then hit the button and Homer will do the rest."""
    st.write(intro_copy)
    st.text_input(label="Title of your story:",
                  key="title",
                  value="Tea in the Ruin",
                  max_chars=100,)
    st.text_area(label="Describe your story here:",
                 height=200,
                 key="premise",
                 value="In the ruins of civilization, after the apocalypse, three friends gather for a picnic.",
                 max_chars=500,
                 )
    st.number_input(label="Number of scenes to tell that story (more scenes means a longer story):",
                    key="num_scenes",
                    min_value=1,
                    max_value=10,
                    value=3,
                    )
    st.slider('Number of (central) characters:',
              min_value=1,
              max_value=10,
              value=3,
              key="num_characters")
    with st.container(border=True, height=500):
        for i in range(st.session_state.get("num_characters")):
            draw_character_input(i)

    if st.button(label="Tell me a story!",
                 key="tell_story"):
        if initialize_story():
            st.switch_page("pages/1_story_builder.py")
        else:
            st.warning("Please fill in all the fields to proceed.",
                       icon="🧐")



if __name__ == "__main__":
    main()
