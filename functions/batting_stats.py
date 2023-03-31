import os
from dotenv import load_dotenv
from sqlalchemy import create_engine as cd
from sqlalchemy.sql import text
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
        "SELECT Round(AVG(R),4), Round(AVG(AVG),4), Round(AVG(OBP),4), Round(AVG(wOBA),4), Round(AVG(wRC),4), Round(AVG(SLG),4), Round(AVG(BABIP),4), Round(AVG(GB),4), Round(AVG(FB),4), Round(AVG(K),4), Round(AVG(BB),4), Round(AVG(OPS),4), Round(AVG(HR),4) FROM Season_Batting_Home_2023")
    league_average_away_query = text(
        "SELECT Round(AVG(R),4), Round(AVG(AVG),4), Round(AVG(OBP),4), Round(AVG(wOBA),4), Round(AVG(wRC),4), Round(AVG(SLG),4), Round(AVG(BABIP),4), Round(AVG(GB),4), Round(AVG(FB),4), Round(AVG(K),4), Round(AVG(BB),4), Round(AVG(OPS),4), Round(AVG(HR),4) FROM Season_Batting_Away_2023")
    connection = engine.connect()
    league_average_home_execution = connection.execute(league_average_home_query)
    league_average_away_execution = connection.execute(league_average_away_query)
    league_average_home = []
    league_average_away = []
    for home_stat in league_average_home_execution:
        league_average_home.append(home_stat)
    for away_stat in league_average_away_execution:
        league_average_away.append(away_stat)

    return league_average_home[0], league_average_away[0]


if __name__ == "__main__":
    # get_team_names()
    league_average()
