import streamlit as st


# Set the page configuration for the About page
st.set_page_config(
    page_title="Despre aplicație",  # Title of the browser tab
    page_icon="ℹ️",  # Icon for the browser tab (info symbol)
    layout="wide",  # Layout of the page ('centered' or 'wide')
    initial_sidebar_state="auto"  # Sidebar state ('auto', 'expanded', 'collapsed')
)
st.title("Despre aplicație")

st.write("Aici povestim despre aplicație")
