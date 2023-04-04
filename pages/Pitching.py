import os.path
import streamlit as st
import sys

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'functions')))
import plotly.graph_objects as go
from pitching_stats import get_team_names, get_starting_pitcher, get_stats

st.set_page_config(layout="wide")
team_names = get_team_names()

st.header("Pitching Stats")


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
                    :red[{stat_name} Team Home Season Average = {season_average_home}]\n
                    :green[{stat_name} Team Away Season Average = {season_average_away}]
                """)


team_name = st.selectbox("Select the team to view their starting pitching stats", team_names)

with st.form(key="pitching_stats"):
    starting_pitchers = get_starting_pitcher(team_name)
    starting_pitcher = st.selectbox("Select the starting pitcher", starting_pitchers)
    starting_pitcher_button = st.form_submit_button("View Stats")
    if starting_pitcher_button:
        league_average, season_average, all_stats = get_stats(team_name, starting_pitcher)

        # ERA Figure
        era_figure = generate_figure(all_stats[0], "ERA", [float(season_average[0][0]), float(season_average[1][0])],
                                     team_name, 1)
        st.plotly_chart(era_figure, use_container_width=True)
        generate_markdown("ERA", [float(season_average[0][0]), float(season_average[1][0])], 1)

        # FIP Figure
        fip_figure = generate_figure(all_stats[1], "FIP", [float(season_average[0][1]), float(season_average[1][1])],
                                     team_name, 1)
        st.plotly_chart(fip_figure, use_container_width=True)
        generate_markdown("FIP", [float(season_average[0][1]), float(season_average[1][1])], 1)

        # xFIP Figure
        xfip_figure = generate_figure(all_stats[2], "xFIP", [float(season_average[0][2]), float(season_average[1][2])],
                                      team_name, 1)
        st.plotly_chart(xfip_figure, use_container_width=True)
        generate_markdown("xFIP", [float(season_average[0][2]), float(season_average[1][2])], 1)

        # AVG Figure
        avg_figure = generate_figure(all_stats[3], "AVG", [float(season_average[0][3]), float(season_average[1][3])],
                                     team_name, 1)
        st.plotly_chart(avg_figure, use_container_width=True)
        generate_markdown("AVG", [float(season_average[0][3]), float(season_average[1][3])], 1)

        # WHIP Figure
        whip_figure = generate_figure(all_stats[4], "WHIP", [float(season_average[0][4]), float(season_average[1][4])],
                                      team_name, 1)
        st.plotly_chart(whip_figure, use_container_width=True)
        generate_markdown("WHIP", [float(season_average[0][4]), float(season_average[1][4])], 1)

        # Runs Figure
        run_figure = generate_figure(all_stats[5], "Runs", [int(season_average[0][5]), int(season_average[1][5])],
                                     team_name, 81)
        st.plotly_chart(run_figure, use_container_width=True)
        generate_markdown("Runs", [int(season_average[0][5]), int(season_average[1][5])], 81)

        # Earned Runs Figure
        Erun_figure = generate_figure(all_stats[6], "Earned Runs",
                                      [int(season_average[0][6]), int(season_average[1][6])],
                                      team_name, 81)
        st.plotly_chart(Erun_figure, use_container_width=True)
        generate_markdown("Earned Runs", [int(season_average[0][6]), int(season_average[1][6])], 81)

        # K Figure
        k_figure = generate_figure(all_stats[7], "K %",
                                   [season_average[0][7].replace("%", ""), season_average[1][7].replace("%", "")],
                                   team_name, 1)
        st.plotly_chart(k_figure, use_container_width=True)
        generate_markdown("K %", [season_average[0][7], season_average[1][7]], 1)

        # BB Figure
        bb_figure = generate_figure(all_stats[8], "BB %",
                                    [season_average[0][8].replace("%", ""), season_average[1][8].replace("%", "")],
                                    team_name, 1)
        st.plotly_chart(bb_figure, use_container_width=True)
        generate_markdown("BB %", [season_average[0][8], season_average[1][8]], 1)

        # HR/9 Figure
        hr9_figure = generate_figure(all_stats[9], "HR/9", [float(season_average[0][9]), float(season_average[1][9])],
                                     team_name, 1)
        st.plotly_chart(hr9_figure, use_container_width=True)
        generate_markdown("HR/9", [float(season_average[0][9]), float(season_average[1][9])], 1)

        # GB Figure
        gb_figure = generate_figure(all_stats[10], "GB%",
                                    [season_average[0][10].replace("%", ""), season_average[1][10].replace("%", "")],
                                    team_name, 1)
        st.plotly_chart(gb_figure, use_container_width=True)
        generate_markdown("GB%", [season_average[0][10], season_average[1][10]], 1)

        # FB Figure
        fb_figure = generate_figure(all_stats[11], "FB%",
                                    [season_average[0][11].replace("%", ""), season_average[1][11].replace("%", "")],
                                    team_name, 1)
        st.plotly_chart(fb_figure, use_container_width=True)
        generate_markdown("FB%", [season_average[0][11], season_average[1][11]], 1)
