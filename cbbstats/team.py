"""Team Statistics

This module is dedictated to querying data and stats for teams. 

"""

import csv
import os
import pkg_resources

from typing import Iterator, Dict

import pandas as pd

DATA_PATH = pkg_resources.resource_filename('cbbstats', 'data/')


def get_season_teams(teams: pd.DataFrame, season: int) -> Iterator[Dict]:
    """Query all team names in a season.

    Args:
        teams:  Kaggle Teams.csv initialized as Pandas DataFrame
        season: tournament year

    Returns:
        team 

    """
    for i, team in teams[(teams['FirstD1Season'] <= season) & (teams['LastD1Season'] >= season)].iterrows():
        yield team.to_dict()


def get_team_stats(stats: pd.DataFrame, season: int, team_id: int) -> Dict:
    """Query stats from team from specified season.

    Args:
        stats:   team_stats.csv initialized as Pandas DataFrame
        season:  year that a tournament took place
        team_id: unique identifier for a team

    Returns:
        series of team stats
    """
    return stats[(stats['kaggle_id'] == team_id) & (stats['season'] == season)].iloc[0].to_dict()


def get_tournament_teams(teams: pd.DataFrame, season: int) -> Iterator[Dict]:
    """Query teams that competed in NCAA Tournament season games.
    
    Args:
        teams:  Kaggle NCAATourneySeeds.csv initialized as Pandas DataFrame
        season: tournament year

    Returns:
        series of team stats

    """
    for team_id in teams[teams['Season'] == season]['TeamID'].unique:
        yield get_team(season, team_id)

