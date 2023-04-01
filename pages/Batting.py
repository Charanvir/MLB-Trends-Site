import os.path
import streamlit as st
import sys

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'functions')))
import plotly.graph_objects as go
from batting_stats import get_team_names, get_stats

st.set_page_config(layout="wide")
team_names = get_team_names()

st.header("Batting Stats")


def generate_figure(stat, stat_name, season_average, team_name, length):
    if length > 1:
        season_average_home = season_average[0] / length
        season_average_away = season_average[1] / length
    else:
        season_average_home = season_average[0]
        season_average_away = season_average[1]
    figure = go.Figure(data=[
        go.Scatter(y=stat, name=stat_name)
    ])
    figure.add_hline(y=season_average_home, line_dash="dash", line_color="red")
    figure.add_hline(y=season_average_away, line_dash="dash", line_color="green")
    figure.update_layout(
        title=f"{stat_name} for {team_name}"
    )
    return figure


def generate_markdown(stat_name, season_average, length):
    if length > 1:
        season_average_home = season_average[0] / length
        season_average_away = season_average[1] / length
    else:
        season_average_home = season_average[0]
        season_average_away = season_average[1]
    st.markdown(f"""
                    :red[{stat_name} Home Season Average = {season_average_home}]\n
                    :green[{stat_name} Away Season Average = {season_average_away}]
                """)


with st.form(key="batting_stats"):
    team_name = st.selectbox("Select the team to view their batting stats", team_names)

    batting_stats_button = st.form_submit_button("View Batting Stats")
    if batting_stats_button:
        st.write(team_name)
        league_average, season_average, all_stats = get_stats(team_name)

        # Runs Figure
        runs_figure = generate_figure(all_stats[0], "Runs", [int(season_average[0][0]), int(season_average[1][0])],
                                      team_name, len(all_stats[0]) / 2)
        st.plotly_chart(runs_figure, use_container_width=True)
        generate_markdown("Runs", [int(season_average[0][0]), int(season_average[1][0])], len(all_stats[0]) / 2)

        # Batting Average Figure
        AVG_figure = generate_figure(all_stats[1], "AVG %", [float(season_average[0][1]), float(season_average[1][1])],
                                     team_name, 1)
        st.plotly_chart(AVG_figure, use_container_width=True)
        generate_markdown("AVG %", [float(season_average[0][1]), float(season_average[1][1])], 1)

        # OBP Figure
        OBP_figure = generate_figure(all_stats[2], "OBP %", [float(season_average[0][2]), float(season_average[1][2])],
                                     team_name, 1)
        st.plotly_chart(OBP_figure, use_container_width=True)
        generate_markdown("OBP %", [float(season_average[0][2]), float(season_average[1][2])], 1)

        # wOBA Figure
        wOBA_figure = generate_figure(all_stats[3], "wOBA %",
                                      [float(season_average[0][3]), float(season_average[1][3])],
                                      team_name, 1)
        st.plotly_chart(wOBA_figure, use_container_width=True)
        generate_markdown("wOBA %", [float(season_average[0][3]), float(season_average[1][3])], 1)

        # wRC Figure
        wRC_figure = generate_figure(all_stats[4], "wRC", [int(season_average[0][4]), int(season_average[1][4])],
                                     team_name, len(all_stats[0]) / 2)
        st.plotly_chart(wRC_figure, use_container_width=True)
        generate_markdown("Runs", [int(season_average[0][4]), int(season_average[1][4])], len(all_stats[0]) / 2)

        # Slugging Figure
        slugging_figure = generate_figure(all_stats[5], "Slugging %",
                                          [float(season_average[0][5]), float(season_average[1][5])],
                                          team_name, 1)
        st.plotly_chart(slugging_figure, use_container_width=True)
        generate_markdown("Slugging %", [float(season_average[0][5]), float(season_average[1][5])], 1)

        # BABIP Figure
        babip_figure = generate_figure(all_stats[6], "BABIP %",
                                       [float(season_average[0][6]), float(season_average[1][6])],
                                       team_name, 1)
        st.plotly_chart(babip_figure, use_container_width=True)
        generate_markdown("BABIP %", [float(season_average[0][6]), float(season_average[1][6])], 1)

        # GB Figure
        GB_figure = generate_figure(all_stats[7], "GB%",
                                    [season_average[0][7].replace("%", ""), season_average[1][7].replace("%", "")],
                                    team_name, 1)
        st.plotly_chart(GB_figure, use_container_width=True)
        generate_markdown("GB%", [season_average[0][7], season_average[1][7]], 1)

        # FB Figure
        FB_figure = generate_figure(all_stats[8], "FB%",
                                    [season_average[0][8].replace("%", ""), season_average[1][8].replace("%", "")],
                                    team_name, 1)
        st.plotly_chart(FB_figure, use_container_width=True)
        generate_markdown("FB%", [season_average[0][8], season_average[1][8]], 1)

        # K Figure
        K_figure = generate_figure(all_stats[9], "K%",
                                   [season_average[0][9].replace("%", ""), season_average[1][9].replace("%", "")],
                                   team_name, 1)
        st.plotly_chart(K_figure, use_container_width=True)
        generate_markdown("K%", [season_average[0][9], season_average[1][9]], 1)

        # BB Figure
        BB_figure = generate_figure(all_stats[10], "BB%",
                                    [season_average[0][10].replace("%", ""), season_average[1][10].replace("%", "")],
                                    team_name, 1)
        st.plotly_chart(BB_figure, use_container_width=True)
        generate_markdown("BB%", [season_average[0][10], season_average[1][10]], 1)

        # OPS Figure
        OPS_figure = generate_figure(all_stats[11], "OPS%",
                                     [float(season_average[0][11]), float(season_average[1][11])],
                                     team_name, 1)
        st.plotly_chart(OPS_figure, use_container_width=True)
        generate_markdown("OPS%", [float(season_average[0][11]), float(season_average[1][11])], 1)

        # HR Figure
        HR_figure = generate_figure(all_stats[12], "HR", [int(season_average[0][12]), int(season_average[1][12])],
                                    team_name, len(all_stats[0]) / 2)
        st.plotly_chart(HR_figure, use_container_width=True)
        generate_markdown("HR", [int(season_average[0][12]), int(season_average[1][12])], len(all_stats[0]) / 2)
