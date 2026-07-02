import streamlit as st


def stat_card(icon, title, value, color="#6366F1"):

    st.markdown(f"""
    <div style="
        background:#1E293B;
        border-radius:18px;
        padding:20px;
        border-left:6px solid {color};
        box-shadow:0px 8px 20px rgba(0,0,0,.25);
        margin-bottom:12px;
    ">
        <h3 style="margin:0;">{icon} {title}</h3>
        <h1 style="margin-top:10px;">{value}</h1>
    </div>
    """, unsafe_allow_html=True)