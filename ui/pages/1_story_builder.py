import streamlit as st


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


if __name__ == "__main__":
    main()