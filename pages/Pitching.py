import os.path
import streamlit as st
import sys

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'functions')))
import plotly.graph_objects as go
from pitching_stats import get_team_names, get_starting_pitcher, get_stats

st.set_page_config(layout="wide")
team_names = get_team_names()

st.header("Pitching Stats")

team_name = st.selectbox("Select the team to view their starting pitching stats", team_names)


with st.form(key="pitching_stats"):
    starting_pitchers = get_starting_pitcher(team_name)
    starting_pitcher = st.selectbox("Select the starting pitcher", starting_pitchers)
    starting_pitcher_button = st.form_submit_button("View Stats")
    if starting_pitcher_button:
        league_average, season_average, all_stats = get_stats(team_name, starting_pitcher)
