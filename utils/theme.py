import streamlit as st


def load_theme():

    st.markdown("""
<style>

/* ==========================================
BACKGROUND
========================================== */

.stApp{
    background:#0F172A;
    color:#F8FAFC;
}

/* ==========================================
SIDEBAR
========================================== */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #334155;
}

/* ==========================================
HEADINGS
========================================== */

h1,h2,h3,h4,h5,h6{
    color:#F8FAFC;
    font-weight:700;
}

/* ==========================================
TEXT
========================================== */

p,label,span{
    color:#CBD5E1;
}

/* ==========================================
BUTTONS
========================================== */

.stButton>button{

    width:100%;

    background:#2563EB;

    color:white;

    border:none;

    border-radius:12px;

    padding:12px;

    font-weight:bold;

    transition:0.3s;
}

.stButton>button:hover{

    background:#1D4ED8;

    transform:translateY(-2px);

}

/* ==========================================
TEXT INPUT
========================================== */

.stTextInput input{

    background:#1E293B;

    color:white;

    border-radius:12px;

    border:1px solid #334155;

}

/* ==========================================
TEXT AREA
========================================== */

.stTextArea textarea{

    background:#1E293B;

    color:white;

    border-radius:12px;

    border:1px solid #334155;

}

/* ==========================================
SELECT BOX
========================================== */

.stSelectbox div[data-baseweb="select"]{

    background:#1E293B;

    border-radius:12px;

}

/* ==========================================
SLIDER
========================================== */

.stSlider{

    padding-top:10px;

}

/* ==========================================
METRIC CARDS
========================================== */

div[data-testid="stMetric"]{

    background:#1E293B;

    padding:20px;

    border-radius:18px;

    border:1px solid #334155;

    box-shadow:0px 8px 25px rgba(0,0,0,.35);

}

/* ==========================================
CHECKBOX
========================================== */

.stCheckbox{

    padding:6px;

}

/* ==========================================
PROGRESS BAR
========================================== */

.stProgress>div>div>div{

    background:#38BDF8;

}

/* ==========================================
INFO / SUCCESS
========================================== */

.stAlert{

    border-radius:15px;

}

/* ==========================================
CONTAINERS
========================================== */

div[data-testid="stVerticalBlock"]{

    gap:1rem;

}

/* ==========================================
SCROLLBAR
========================================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#475569;

    border-radius:20px;

}

::-webkit-scrollbar-track{

    background:#0F172A;

}

</style>
""", unsafe_allow_html=True)