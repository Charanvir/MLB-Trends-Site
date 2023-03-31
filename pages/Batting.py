import os.path
import streamlit as st
import sys
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'functions')))
import plotly.graph_objects as go
from batting_stats import get_team_names

st.set_page_config(layout="wide")
team_names = get_team_names()

st.header("Batting Stats")

with st.form(key="batting_stats"):
    team_name = st.selectbox("Select the team to view their batting stats", team_names)

    batting_stats_button = st.form_submit_button("View Batting Stats")
    if batting_stats_button:
        st.write(team_name)
