import streamlit as st

from util.status import Status
from structures.enums import StatusType
from logic.core_logic import write_story

st.set_page_config(
    layout="wide",
    page_title="Homer the Storyteller",
    page_icon="🍩",
)


def display_story(story_graph):
    st.header(story_graph["title"])
    for i, scene in enumerate(story_graph["scenes"]):
        with st.expander(f"Scene {i+1} ({len(scene.text.split())} words)", icon="📜"):
            st.write(scene.text)
    for i, scene_desc in enumerate(story_graph["scene_descriptions"]):
        with st.expander(f"Scene Desc. {i+1}"):
            st.write(scene_desc)


def main():
    st.header("Homer the Storyteller")
    if not st.session_state["the_story"]:
        st.warning("Something has gone wrong--please go back to the homepage and start over.",
                   icon="🥸")
        return
    message = """Homer is composing your story. This may take a bit as Homer must dream up each scene, and then revise 
    it to make sure that it is vivid, compelling, true to the characters, and just generally worthy of your story. Watch
    the space below to see what Homer is up to."""
    st.write(message)
    status_box = st.status(label=f'Composing "{st.session_state["the_story"].title}"...',
                           expanded=True,
                           state="running")
    Status().initialize(status_box)
    finished_story = write_story(st.session_state["the_story"])

    if not finished_story:
        st.warning("Something has gone wrong--please go back to the homepage and try to generate a story again.",
                   icon="🥸")
        return

    st.session_state["the_story"] = finished_story
    Status().update(StatusType.CONCLUDE_SUCCESS, "Composition complete.")
    st.success("Your story is complete! You can read it below.")
    display_story(finished_story)


if __name__ == "__main__":
    main()
