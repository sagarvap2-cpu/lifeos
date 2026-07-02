import streamlit as st

from database import (
    add_habit,
    get_habits,
    save_habit_log,
    get_habit_status,
    delete_habit
)


def show_habits():

    # ==========================================
    # Header
    # ==========================================

    st.title("✅ Habit Tracker")
    st.caption("Small habits. Big results.")

    st.divider()

    # ==========================================
    # Add Habit
    # ==========================================

    st.subheader("➕ Add New Habit")

    col1, col2 = st.columns([3, 2])

    with col1:
        habit_name = st.text_input(
            "Habit Name",
            placeholder="Example: Learn Python"
        )

    with col2:
        category = st.selectbox(
            "Category",
            [
                "💻 Productivity",
                "📚 Study",
                "🏃 Fitness",
                "❤️ Health",
                "📖 Personal"
            ]
        )

    if st.button("➕ Add Habit", use_container_width=True):

        if habit_name.strip():

            add_habit(habit_name, category)

            st.success("Habit added successfully!")

            st.rerun()

        else:

            st.warning("Please enter a habit name.")

    st.divider()

    # ==========================================
    # Habit List
    # ==========================================

    st.subheader("📋 Today's Habits")

    habits = get_habits()

    if len(habits) == 0:

        st.info("No habits added yet.")

        return

    completed = 0

    for habit in habits:

        with st.container(border=True):

            st.markdown(f"### {habit['habit_name']}")

            st.caption(f"🏷️ {habit['category']}")

            checked = st.checkbox(
                "Completed Today",
                value=get_habit_status(habit["id"]),
                key=f"habit_{habit['id']}"
            )

            save_habit_log(
                habit["id"],
                int(checked)
            )

            if checked:
                completed += 1

            st.write("🔥 Streak: Coming Soon")

            col1, col2 = st.columns(2)

            with col1:

                st.button(
                    "✏️ Edit",
                    key=f"edit_{habit['id']}",
                    use_container_width=True,
                    disabled=True
                )

            with col2:

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{habit['id']}",
                    use_container_width=True
                ):

                    delete_habit(habit["id"])

                    st.success("Habit deleted successfully!")

                    st.rerun()

    # ==========================================
    # Progress
    # ==========================================

    total = len(habits)

    progress = completed / total

    st.divider()

    st.subheader("📊 Today's Progress")

    m1, m2, m3 = st.columns(3)

    m1.metric(
        "✅ Completed",
        completed
    )

    m2.metric(
        "📌 Remaining",
        total - completed
    )

    m3.metric(
        "🎯 Progress",
        f"{int(progress * 100)}%"
    )

    st.progress(progress)

    if progress == 1:

        st.success("🏆 Amazing! Every habit completed today!")

    elif progress >= 0.75:

        st.success("🔥 Fantastic! You're almost done!")

    elif progress >= 0.50:

        st.info("💪 Great progress! Keep going!")

    elif progress > 0:

        st.warning("🚀 Every completed habit counts.")

    else:

        st.error("Start your first habit today 💙")