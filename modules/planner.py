import streamlit as st

from database import (
    add_task,
    get_tasks,
    update_task,
    delete_task
)


def show_planner():

    st.title("📅 Planner")
    st.caption("Plan your day. Achieve your goals.")

    st.divider()

    # ==========================================
    # Add Task
    # ==========================================

    st.subheader("➕ Add New Task")

    col1, col2 = st.columns([3, 1])

    with col1:
        task = st.text_input(
            "Task",
            placeholder="Example: Complete LifeOS AI"
        )

    with col2:
        task_time = st.time_input("Time")

    priority = st.selectbox(
        "Priority",
        [
            "🔴 High",
            "🟡 Medium",
            "🟢 Low"
        ]
    )

    if st.button("➕ Add Task", use_container_width=True):

        if task.strip():

            add_task(
                task,
                str(task_time),
                priority
            )

            st.success("Task Added Successfully!")

            st.rerun()

        else:

            st.warning("Enter a task name.")

    st.divider()

    # ==========================================
    # Tasks
    # ==========================================

    st.subheader("📋 Today's Tasks")

    tasks = get_tasks()

    if len(tasks) == 0:

        st.info("No tasks yet.")

        return

    completed = 0

    for task in tasks:

        with st.container(border=True):

            st.markdown(f"### {task['task']}")

            st.caption(f"🕒 {task['task_time']}")

            st.caption(task["priority"])

            checked = st.checkbox(
                "Completed",
                value=bool(task["completed"]),
                key=f"task_{task['id']}"
            )

            update_task(
                task["id"],
                int(checked)
            )

            if checked:
                completed += 1

            if st.button(
                "🗑 Delete",
                key=f"delete_task_{task['id']}",
                use_container_width=True
            ):

                delete_task(task["id"])

                st.success("Task Deleted!")

                st.rerun()

    st.divider()

    progress = completed / len(tasks)

    st.subheader("📊 Today's Progress")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Completed",
        completed
    )

    c2.metric(
        "Remaining",
        len(tasks) - completed
    )

    c3.metric(
        "Progress",
        f"{int(progress * 100)}%"
    )

    st.progress(progress)

    if progress == 1:
        st.success("🏆 All tasks completed!")

    elif progress >= 0.5:
        st.info("💪 Great progress!")

    else:
        st.warning("🚀 Keep going!")