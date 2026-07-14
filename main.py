import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import Home
import Companies
import ratings
import locations
import roles
import experience
import skills
import freshers
import cleaned_dataset

st.set_page_config(
    page_title="Indian Tech Jobs Dashboard",
    page_icon="📊",
    layout="wide"
)

with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Home",
            "Companies",
            "Ratings",
            "Locations",
            "Roles",
            "Experience & Work Mode",
            "Skills",
            "Freshers Insights",
            "Cleaned Dataset"
        ],
        icons=[
            "house",
            "building",
            "star",
            "geo-alt",
            "briefcase",
            "clock-history",
            "tools",
            "person-workspace",
            "table"
        ],
        menu_icon="list",
        default_index=0   
    )

if selected == "Home":
    Home.app()

elif selected == "Companies":
    Companies.comp()

elif selected == "Ratings":
    ratings.rate()

elif selected == "Locations":
    locations.loc()

elif selected == "Roles":
    roles.role()

elif selected == "Experience & Work Mode":
    experience.exp()
    

elif selected == "Skills":
    skills.skill()

elif selected == "Freshers Insights":
    freshers.fresher()

elif selected == "Cleaned Dataset":
    cleaned_dataset.cleaned()