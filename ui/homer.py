import streamlit as st

# Get absolute path to the project root (otherwise package importing doesn't work correctly)
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


# Define the application
pages = {
    "" : [st.Page("0_main.py", title="Homepage", icon="🍩️")],
    "Story Builder" : [
        st.Page("1_story_builder.py", title="Story Builder", icon="📏"),
    ],
}

pg = st.navigation(pages)
pg.run()