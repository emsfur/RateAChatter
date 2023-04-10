import streamlit as st
import plotly.express as px

defArgs = ['funny', 'annoying', 'bannable', 'cringe', 'nice',  'interesting']

# initialize items
for i in range(6):
    if f'arg{i}' not in st.session_state:
        st.session_state[f'arg{i}'] = defArgs[i]
if 'username' not in st.session_state:
    st.session_state['username'] = ""

def resetInput():
    st.session_state['username'] = ""
    for i in range(6):
        st.session_state['val' + str(i)] = 0

with st.sidebar:
    useTab, editTab = st.tabs(["Use", "Edit"])

    # handles use mode
    sliderDiv = useTab.empty();
    if useTab.button('reset', use_container_width=True):
        resetInput()
    with sliderDiv.container():
        st.text_input('Username', key='username')
        for i in range(6):
            st.slider(st.session_state[f'arg{i}'], 0, 10, key='val' + str(i))

    # handles edit mode
    with editTab:
        for i in range(6):
            st.text_input(' ',value=st.session_state[f'arg{i}'], key=f'arg{i}')

data = {'r':[st.session_state['val' + str(i)] for i in range(6)],
        'theta':[st.session_state[f'arg{i}'] for i in range(6)]}

fig = px.line_polar(data, r=data['r'], theta=data['theta'], 
                    title='<span style="font-size: 50px;">' + st.session_state['username'] + '</span>', 
                    line_close=True, template='plotly_dark', width=1000, height=700, range_r=[0,10])

fig.update_traces(fill='toself')
fig.update_layout(font=dict(
    family='Open Sans',
    size=20,
    color='white'),
    margin=dict(l=100, r=100, t=100, b=1)
)

st.plotly_chart(fig, use_container_width=True)
