import pandas as pd
import plotly.express as px

def weekly_chart():

    df = pd.DataFrame({

        "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],

        "Completion":[60,75,82,70,91,87,76]

    })

    fig = px.area(

        df,

        x="Day",

        y="Completion",

        template="plotly_dark"

    )

    fig.update_layout(

        paper_bgcolor="#0F172A",

        plot_bgcolor="#0F172A",

        height=330,

        margin=dict(l=10,r=10,t=20,b=10)

    )

    return fig