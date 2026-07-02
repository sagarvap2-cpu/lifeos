import streamlit as st

from database import (
    total_habits,
    total_tasks,
    total_goals,
    total_journal,
    get_life_score
)

from utils.charts import weekly_chart


def show_analytics():

    st.title("📊 Analytics")
    st.caption("Track your personal productivity.")

    st.divider()

    score = get_life_score()

    st.metric("⭐ Life Score", f"{score}%")

    st.progress(score / 100)

    st.divider()

    st.subheader("📈 Weekly Progress")

    st.plotly_chart(
        weekly_chart(),
        use_container_width=True
    )

    st.divider()

    st.subheader("📊 Overall Statistics")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "✅ Habits",
            total_habits()
        )

        st.metric(
            "📅 Tasks",
            total_tasks()
        )

    with c2:

        st.metric(
            "🎯 Goals",
            total_goals()
        )

        st.metric(
            "📖 Journal",
            total_journal()
        )

    st.divider()

    if score >= 80:

        st.success("🔥 You're doing amazing this week!")

    elif score >= 50:

        st.info("💪 Keep building momentum!")

    else:

        st.warning("🚀 Let's improve your consistency!")