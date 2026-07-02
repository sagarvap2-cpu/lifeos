import streamlit as st


def stat_card(title, value, icon):
    html = f"""
    <div style="
        background-color:#1E293B;
        border-radius:15px;
        padding:20px;
        border:1px solid #334155;
        box-shadow:0 4px 10px rgba(0,0,0,0.3);
        text-align:center;
        margin-bottom:15px;
    ">
        <h4 style="margin:0;color:white;">{icon} {title}</h4>
        <h1 style="margin-top:10px;color:#60A5FA;">{value}</h1>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)