import streamlit as st

from database import (
    add_goal,
    get_goals,
    update_goal,
    delete_goal
)


def show_goals():

    st.title("🎯 Goals")

    st.caption("Turn your dreams into achievements.")

    st.divider()

    # ====================================
    # Add Goal
    # ====================================

    st.subheader("➕ Add New Goal")

    goal = st.text_input(
        "Goal",
        placeholder="Example: Become a Python Developer"
    )

    if st.button(
        "➕ Add Goal",
        use_container_width=True
    ):

        if goal.strip():

            # status = 0 (Not Completed)
            add_goal(goal)

            st.success("Goal Added Successfully!")

            st.rerun()

        else:

            st.warning("Please enter a goal.")

    st.divider()

    # ====================================
    # Goal List
    # ====================================

    goals = get_goals()

    st.subheader("🎯 My Goals")

    if len(goals) == 0:

        st.info("No goals added yet.")

        return

    completed = 0

    for goal in goals:

        with st.container(border=True):

            checked = st.checkbox(
                goal["goal"],
                value=bool(goal["status"]),
                key=f"goal_{goal['id']}"
            )

            update_goal(
                goal["id"],
                int(checked)
            )

            if checked:
                completed += 1

            if st.button(
                "🗑 Delete Goal",
                key=f"delete_goal_{goal['id']}",
                use_container_width=True
            ):

                delete_goal(goal["id"])

                st.success("Goal Deleted!")

                st.rerun()

    st.divider()

    progress = completed / len(goals)

    st.subheader("📊 Goal Progress")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Completed",
        completed
    )

    c2.metric(
        "Remaining",
        len(goals) - completed
    )

    c3.metric(
        "Progress",
        f"{int(progress * 100)}%"
    )

    st.progress(progress)

    if progress == 1:

        st.success("🏆 Amazing! Every goal completed!")

    elif progress >= 0.5:

        st.info("💪 Great progress!")

    else:

        st.warning("🚀 Keep moving forward!")