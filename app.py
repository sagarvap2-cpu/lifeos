import streamlit as st
from utils.theme import load_theme
from utils.sidebar import sidebar
from modules.dashboard import show_dashboard
from modules.habits import show_habits
from modules.planner import show_planner
from modules.goals import show_goals
from modules.analytics import show_analytics
from modules.settings import show_settings
from modules.journal import show_journal
from modules.coding import show_coding
st.set_page_config(
    page_title="LifeOS AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_theme()

selected = sidebar()

if selected == "Dashboard":
    show_dashboard()

elif selected == "Habits":
    show_habits()

elif selected == "Planner":
    show_planner()

elif selected == "Goals":
    show_goals()

elif selected == "Journal":
    show_journal()

elif selected == "Coding":
    show_coding()

elif selected == "Analytics":
    show_analytics()

elif selected == "Settings":
    show_settings()