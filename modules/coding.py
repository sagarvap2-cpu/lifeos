import streamlit as st


def show_coding():

    st.title("💻 Coding Workspace")

    st.caption("Code. Learn. Build. Repeat.")

    st.divider()

    # ==========================================
    # Current Project
    # ==========================================

    st.subheader("🚀 Current Project")

    st.success("LifeOS AI")

    st.divider()

    # ==========================================
    # Coding Notes
    # ==========================================

    st.subheader("📝 Coding Notes")

    st.text_area(
        "Today's Notes",
        placeholder="Write bugs, ideas, or today's coding plan...",
        height=220
    )

    st.button(
        "💾 Save Notes",
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # Coding Checklist
    # ==========================================

    st.subheader("✅ Today's Checklist")

    st.checkbox("Fix Bugs")

    st.checkbox("Write New Feature")

    st.checkbox("Git Commit")

    st.checkbox("Push to GitHub")

    st.checkbox("Deploy Project")

    st.divider()

    # ==========================================
    # Quick Commands
    # ==========================================

    st.subheader("⚡ Git Commands")

    st.code("""git add .
git commit -m "Update Project"
git push""")

    st.divider()

    # ==========================================
    # Daily Motivation
    # ==========================================

    st.subheader("🔥 Developer Mindset")

    st.info(
        "Every bug you fix makes you a better developer."
    )

    st.success(
        "Keep shipping. Progress beats perfection."
    )