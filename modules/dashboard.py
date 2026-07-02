import random
import streamlit as st

from database import (
    get_today_progress,
    get_life_score,
    get_habits,
    get_habit_status
)

from utils.helpers import get_greeting, today_date
from utils.charts import weekly_chart
from utils.ui import stat_card


def show_dashboard():

    # ==========================================
    # Header
    # ==========================================

    st.title("🚀 LifeOS AI")

    st.markdown(f"## {get_greeting()}, Sagar 👋")

    st.caption(f"📅 {today_date()}")

    st.info(
        "🎯 Today's Mission: Complete your habits, finish your tasks, and improve your Life Score."
    )

    st.divider()

    # ==========================================
    # Statistics
    # ==========================================

    completed, total, progress = get_today_progress()
    life_score = get_life_score()

    col1, col2 = st.columns(2)

    with col1:
        stat_card(
            "⭐ Life Score",
            f"{life_score}%",
            "⭐"
        )

    with col2:
        stat_card(
            "🎯 Today's Progress",
            f"{progress}%",
            "🎯"
        )

    col3, col4 = st.columns(2)

    with col3:
        stat_card(
            "✅ Habits",
            f"{completed}/{total}",
            "✅"
        )

    with col4:
        stat_card(
            "🔥 Streak",
            "Coming Soon",
            "🔥"
        )

    # ==========================================
    # Motivation
    # ==========================================

    if life_score >= 80:

        st.success("🔥 Amazing! You're having an excellent day!")

    elif life_score >= 50:

        st.info("💪 Great progress! Keep pushing!")

    else:

        st.warning("🚀 Complete a few more habits to increase your Life Score!")

    st.divider()

    # ==========================================
    # Daily Focus
    # ==========================================

    st.subheader("🎯 Daily Focus")

    st.success(
        "Complete all habits, finish your planner tasks, and become 1% better today."
    )

    st.divider()

    # ==========================================
    # Main Section
    # ==========================================

    left, right = st.columns(2)

    with left:

        st.subheader("✅ Today's Habits")

        habits = get_habits()

        if len(habits) == 0:

            st.info("No habits added yet.")

        else:

            st.caption(f"{completed} of {total} habits completed today")

            for habit in habits:

                st.checkbox(
                    habit["habit_name"],
                    value=get_habit_status(habit["id"]),
                    disabled=True,
                    key=f"dashboard_{habit['id']}"
                )

    with right:

        st.subheader("📈 Weekly Progress")

        st.plotly_chart(
            weekly_chart(),
            use_container_width=True
        )

        st.caption("Consistency is the key to success.")

    st.divider()

    # ==========================================
    # Bottom Section
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📅 Today's Planner")

        planner = [

            "💻 Coding Session",

            "🎓 College Work",

            "🚀 Build LifeOS AI",

            "🏃 Workout",

            "📖 Read 20 Minutes"

        ]

        for task in planner:

            st.markdown(f"✅ {task}")

    with col2:

        st.subheader("💬 Quote of the Day")

        quotes = [

            "Discipline beats motivation.",

            "Small improvements every day lead to remarkable results.",

            "Consistency creates greatness.",

            "Win today. Repeat tomorrow.",

            "Success is built one day at a time.",

            "Don't stop when you're tired. Stop when you're done."

        ]

        st.success(f"💡 {random.choice(quotes)}")

    st.divider()

    # ==========================================
    # Footer
    # ==========================================

    st.caption(
        "🚀 LifeOS AI v1.0 | Built with ❤️ using Python, Streamlit & SQLite"
    )