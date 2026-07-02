from streamlit_option_menu import option_menu
import streamlit as st
from database import get_life_score


def sidebar():

    life_score = get_life_score()

    with st.sidebar:

        # ==========================================
        # Logo
        # ==========================================

        st.markdown(
            """
            # 🚀 LifeOS AI
            ### Your Personal Productivity OS
            """
        )

        st.divider()

        # ==========================================
        # Navigation
        # ==========================================

        selected = option_menu(

            menu_title=None,

            options=[
                "Dashboard",
                "Habits",
                "Planner",
                "Goals",
                "Journal",
                "Coding",
                "Analytics",
                "Settings"
            ],

            icons=[
                "house-fill",
                "check2-square",
                "calendar-event",
                "bullseye",
                "journal-bookmark-fill",
                "code-slash",
                "graph-up-arrow",
                "gear-fill"
            ],

            default_index=0,

            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#0f172a",
                },
                "icon": {
                    "color": "#38bdf8",
                    "font-size": "18px",
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "4px",
                    "padding": "12px",
                    "--hover-color": "#1e293b",
                    "border-radius": "10px",
                },
                "nav-link-selected": {
                    "background-color": "#2563eb",
                    "color": "white",
                    "font-weight": "bold",
                },
            }

        )

        st.divider()

        # ==========================================
        # Life Score
        # ==========================================

        st.markdown("### ⭐ Life Score")

        st.progress(life_score / 100)

        st.success(f"{life_score}%")

        st.divider()

        # ==========================================
        # Version
        # ==========================================

        st.caption("🚀 LifeOS AI")
        st.caption("Version 1.0")

    return selected