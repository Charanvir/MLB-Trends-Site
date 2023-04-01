import os
from dotenv import load_dotenv
from sqlalchemy import create_engine as cd
from sqlalchemy.sql import text
import sqlalchemy as sa
import pandas as pd

load_dotenv()

user = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")
database_name = os.getenv("MYSQL_DATABASE")
aws_URL = os.getenv("AWS_DATABASE_URL")

engine = cd(f"mysql://{user}:{password}@{aws_URL}:3306/{database_name}")


def get_team_names():
    connection = engine.connect()
    team_name_query = text("SELECT Team FROM Season_Batting_Away_2022 ORDER BY Team ASC")
    team_name_execution = connection.execute(team_name_query)
    team_names = []
    for team in team_name_execution:
        team_names.append(team[0])
    connection.close()
    return tuple(team_names)


def league_average():
    league_average_home_query = text(
        "SELECT Round(AVG(R),4), Round(AVG(AVG),4), Round(AVG(OBP),4), Round(AVG(wOBA),4), Round(AVG(wRC),4), Round(AVG(SLG),4), Round(AVG(BABIP),4), Round(AVG(GB),4), Round(AVG(FB),4), Round(AVG(K),4), Round(AVG(BB),4), Round(AVG(OPS),4), Round(AVG(HR),4) FROM Season_Batting_Home_2022")
    league_average_away_query = text(
        "SELECT Round(AVG(R),4), Round(AVG(AVG),4), Round(AVG(OBP),4), Round(AVG(wOBA),4), Round(AVG(wRC),4), Round(AVG(SLG),4), Round(AVG(BABIP),4), Round(AVG(GB),4), Round(AVG(FB),4), Round(AVG(K),4), Round(AVG(BB),4), Round(AVG(OPS),4), Round(AVG(HR),4) FROM Season_Batting_Away_2022")
    connection = engine.connect()
    league_average_home_execution = connection.execute(league_average_home_query)
    league_average_away_execution = connection.execute(league_average_away_query)
    league_average_home = []
    league_average_away = []
    for home_stat in league_average_home_execution:
        league_average_home.append(home_stat)
    for away_stat in league_average_away_execution:
        league_average_away.append(away_stat)
    connection.close()
    return [league_average_home[0], league_average_away[0]]


def season_average(teamName):
    season_average_home_query = text(
        f"SELECT R, AVG, OBP, wOBA, wRC, SLG, BABIP, GB, FB, K, BB, OPS, HR FROM Season_Batting_Home_2022 WHERE Team = '{teamName}'"
    )
    season_average_away_query = text(
        f"SELECT R, AVG, OBP, wOBA, wRC, SLG, BABIP, GB, FB, K, BB, OPS, HR FROM Season_Batting_Away_2022 WHERE Team = '{teamName}'"
    )
    connection = engine.connect()
    season_average_home_execution = connection.execute(season_average_home_query)
    season_average_away_execution = connection.execute(season_average_away_query)
    season_average_home = []
    season_average_away = []
    for home_stat in season_average_home_execution:
        season_average_home.append(home_stat)
    for away_stat in season_average_away_execution:
        season_average_away.append(away_stat)
    connection.close()
    return [season_average_home[0], season_average_away[0]]


def all_stats(teamName):
    stat_query = text(
        f"SELECT R, AVG, OBP, wOBA, wRC, SLG, BABIP, GB, FB, K, BB, OPS, HR FROM {teamName}_Batting_2022"
    )
    connection = engine.connect()
    stat_execution = connection.execute(stat_query)
    R = []
    AVG = []
    OBP = []
    wOBA = []
    wRC = []
    SLG = []
    BABIP = []
    GB = []
    FB = []
    K = []
    BB = []
    OPS = []
    HR = []
    for stat in stat_execution:
        R.append(stat[0])
        AVG.append(stat[1])
        OBP.append(stat[2])
        wOBA.append(stat[3])
        wRC.append(stat[4])
        SLG.append(stat[5])
        BABIP.append(stat[6])
        GB.append(stat[7])
        FB.append(stat[8])
        K.append(stat[9])
        BB.append(stat[10])
        OPS.append(stat[11])
        HR.append(stat[12])
    connection.close()
    return [R, AVG, OBP, wOBA, wRC, SLG, BABIP, GB, FB, K, BB, OPS, HR]


def get_stats(teamName):
    league_average_stats = league_average()
    season_average_stats = season_average(teamName)
    season_stats = all_stats(teamName)
    return league_average_stats, season_average_stats, season_stats


if __name__ == "__main__":
    stats = all_stats("TOR")
    print(stats)
