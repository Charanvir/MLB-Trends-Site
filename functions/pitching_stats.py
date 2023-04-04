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


def get_starting_pitcher(teamName):
    starting_pitcher_query = text(
        f"SELECT DISTINCT Name FROM {teamName}_Pitching_2022"
    )
    connection = engine.connect()
    starting_pitcher_execution = connection.execute(starting_pitcher_query)
    starting_pitchers = []
    for starting_pitcher in starting_pitcher_execution:
        starting_pitchers.append(starting_pitcher[0])
    connection.close()
    return tuple(starting_pitchers)


def league_average():
    league_average_home_query = text(
        "SELECT ROUND(AVG(ERA), 4), ROUND(AVG(FIP), 4), ROUND(AVG(xFIP), 4), ROUND(AVG(AVG), 4), ROUND(AVG(WHIP), 4), ROUND(AVG(R), 4), ROUND(AVG(ER), 4), ROUND(AVG(K),4 ), ROUND(AVG(BB), 4), ROUND(AVG(HR9), 4), ROUND(AVG(GB),4 ), ROUND(AVG(FB), 4) FROM Season_Pitching_Home_2022"
    )
    league_average_away_query = text(
        "SELECT ROUND(AVG(ERA), 4), ROUND(AVG(FIP), 4), ROUND(AVG(xFIP), 4), ROUND(AVG(AVG), 4), ROUND(AVG(WHIP), 4), ROUND(AVG(R), 4), ROUND(AVG(ER), 4), ROUND(AVG(K),4 ), ROUND(AVG(BB), 4), ROUND(AVG(HR9), 4), ROUND(AVG(GB),4 ), ROUND(AVG(FB), 4) FROM Season_Pitching_Away_2022"
    )
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
        f"SELECT ERA, FIP, xFIP, AVG, WHIP, R, ER, K, BB, HR9, GB, FB FROM Season_Pitching_Home_2022 WHERE Team = '{teamName}'"
    )
    season_average_away_query = text(
        f"SELECT ERA, FIP, xFIP, AVG, WHIP, R, ER, K, BB, HR9, GB, FB FROM Season_Pitching_Away_2022 WHERE Team = '{teamName}'"
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


def starting_pitcher_stats(teamName, startingPitcher):
    season_average_pitcher_query = text(
        f"SELECT ERA, FIP, xFIP, AVG, WHIP, R, ER, K, BB, HR9, GB, FB FROM {teamName}_Pitching_2022 WHERE Name = '{startingPitcher}'"
    )
    connection = engine.connect()
    season_average_pitcher_execution = connection.execute(season_average_pitcher_query)
    ERA = []
    FIP = []
    xFIP = []
    AVG = []
    WHIP = []
    R = []
    ER = []
    K = []
    BB = []
    HR9 = []
    GB = []
    FB = []
    for stat in season_average_pitcher_execution:
        ERA.append(stat[0])
        FIP.append(stat[1])
        xFIP.append(stat[2])
        AVG.append(stat[3])
        WHIP.append(stat[4])
        R.append(stat[5])
        ER.append(stat[6])
        K.append(stat[7])
        BB.append(stat[8])
        HR9.append(stat[9])
        GB.append(stat[10])
        FB.append(stat[11])
    connection.close()
    return [ERA, FIP, xFIP, AVG, WHIP, R, ER, K, BB, HR9, GB, FB]


def get_stats(teamName, startingPitcher):
    league_average_stats = league_average()
    season_average_stats = season_average(teamName)
    season_stats = starting_pitcher_stats(teamName, startingPitcher)
    return league_average_stats, season_average_stats, season_stats


if __name__ == "__main__":
    print(starting_pitcher_stats("TOR", "Jose Berrios"))
