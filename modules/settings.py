import streamlit as st


def show_settings():

    st.title("⚙️ Settings")

    st.caption("LifeOS AI Configuration")

    st.divider()

    st.subheader("👤 Profile")

    st.text_input(
        "Name",
        value="Sagar"
    )

    st.text_input(
        "Goal",
        value="Become an AI Engineer"
    )

    st.divider()

    st.subheader("🌙 Theme")

    st.success("Dark Theme Enabled")

    st.divider()

    st.subheader("📦 App")

    st.info("""
LifeOS AI

Version 1.0

Built using

• Python

• Streamlit

• SQLite
""")

    st.divider()

    st.button(
        "🗑 Reset Database",
        use_container_width=True
    )