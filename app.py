import streamlit as st

from streamlit_option_menu import option_menu
from Pages.CSS.generalStyle import create_style
from Pages import complaint, home

#from qdrant_client import models
#import pandas as pd
#from json import loads
st.set_page_config(page_title="Complaint Matching",
                   layout="wide", initial_sidebar_state="collapsed")

st.markdown(create_style(), unsafe_allow_html=True)

# Title
col1, col2 = st.columns([1, 5])
with col1:
    st.image("Static/logo.png")
with col2:
    selected = option_menu("Complaint Matching with QdrantDB", ["Home", "Complaint Matching",],
                           icons=["caret-right-fill", "caret-right-fill"], menu_icon="cast", orientation="horizontal", styles={
        "container": {"background-color": "#FFF", "border-radius": "0"},
        "menu-title": {"font-size": "24px", "color": "#333", "font-family": "'Open Sans', sans-serif", "font-weight": "600"},
        "nav-link": {"font-size": "24px", "color": "#333", "font-family": "'Open Sans', sans-serif", "font-weight": "500", "--hover-color": "#999"},
        "nav-link-selected": {"background-color": "#6cd4f4", "color": "#FFF"}
    }, default_index=0)


if selected == "Home":
    home.create_page()

if selected == "Complaint Matching":
    complaint.create_page()
