import streamlit as st

from util.status import Status
from structures.enums import StatusType

st.set_page_config(
    layout="wide",
    page_title="Homer the Storyteller",
    page_icon="🍩",
)


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
    status_box = st.status(label=f"Composing the {st.session_state["the_story"].title}...",
                           expanded=True,
                           state="running")
    Status().initialize(status_box)
    Status().status_box.write("Does it work this way?")
    Status().update(type=StatusType.MESSAGE, message="Just a test of the output singleton")
    status_box.write("This is a different test of the status box.")
    # finished_story = write_story(st.session_state["the_story"])



if __name__ == "__main__":
    main()