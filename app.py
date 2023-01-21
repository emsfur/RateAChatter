import streamlit as st

import plotly.express as px
import pandas as pd

arg1 = 'funny'
arg2 = 'annoying'
arg3 = 'bannable'
arg4 = 'cringe'
arg5 = 'gilf worthy'
arg6 = 'interesting'

with st.sidebar:
    name = st.text_input(label='Username')
    val1 = st.slider(arg1, 0, 10)
    val2 = st.slider(arg2, 0, 10)
    val3 = st.slider(arg3, 0, 10)
    val4 = st.slider(arg4, 0, 10)
    val5 = st.slider(arg5, 0, 10)
    val6 = st.slider(arg6, 0, 10)

# st.title("Balls")

df = pd.DataFrame(dict(
    r=[val1, val2, val3, val4, val5, val6],
    theta=[arg1, arg2, arg3, arg4, arg5, arg6]))

fig = px.line_polar(df, r='r', theta='theta', title='<span style="font-size: 50px;">' + name + '</span>', line_close=True, template='plotly_dark', width=1000, height=700,range_r=[0,10])
fig.update_traces(fill='toself')
fig.update_layout(font=dict(
        family='Open Sans',
        size=20,
        color='white'
))

# fig.update_layout(title_pad=dict(l=100,t=0, r=0, b=0))

fig.update_layout(
    margin=dict(l=100, r=100, t=100, b=1),
)



st.plotly_chart(fig, use_container_width=True)
