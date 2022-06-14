import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv(r'PhaseII_atleastoneknownivnestor.csv',index_col=[0])

fig = px.scatter_3d(df,x="enterprise value", y="cash and marketable", z="cash burn (runway)",
              color='Name')
fig.show()
st.title('Hello there!')
st.header('Welcome to the Pivotal Onco Distressed Asset Analyzer')
st.subheader('''
    :
    This 3D scatterpolot that is based on 92 Onco companies-
    Only 16 of which
    that have passed Phase 2 trial, are between 
    50-300 Million market cap and have at least
    one well known major investor.

    Please make sure to click on full screen icon '< >'
    located at the top right corner of the graph.
''')
st.plotly_chart(fig)
