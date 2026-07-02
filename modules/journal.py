import streamlit as st

from database import (
    add_journal,
    get_journal
)


def show_journal():

    st.title("📖 Daily Journal")

    st.caption("Reflect today. Improve tomorrow.")

    st.divider()

    # ==========================================
    # New Entry
    # ==========================================

    st.subheader("✍️ Today's Reflection")

    mood = st.selectbox(
        "😊 Mood",
        [
            "😁 Excellent",
            "😊 Happy",
            "😐 Normal",
            "😔 Sad",
            "😴 Tired"
        ]
    )

    energy = st.slider(
        "⚡ Energy Level",
        1,
        10,
        7
    )

    note = st.text_area(
        "📝 What happened today?",
        height=180,
        placeholder="Write your thoughts..."
    )

    if st.button(
        "💾 Save Journal",
        use_container_width=True
    ):

        if note.strip():

            add_journal(
                mood,
                energy,
                note
            )

            st.success("Journal Saved Successfully!")

            st.rerun()

        else:

            st.warning("Write something before saving.")

    st.divider()

    # ==========================================
    # Previous Entries
    # ==========================================

    st.subheader("📚 Previous Entries")

    journals = get_journal()

    if len(journals) == 0:

        st.info("No journal entries yet.")

        return

    for journal in journals:

        with st.container(border=True):

            st.markdown(f"### {journal['mood']}")

            st.caption(
                f"⚡ Energy : {journal['energy']}/10"
            )

            st.write(journal["note"])

            st.caption(
                f"📅 {journal['journal_date']}"
            )