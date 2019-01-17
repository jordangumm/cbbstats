"""Team Statistics

This module is dedictated to querying data and stats for teams. 

"""

import csv
import os
import pkg_resources

from typing import Iterator, Dict

import pandas as pd

DATA_PATH = pkg_resources.resource_filename('cbbstats', 'data/')


def get_teams(season: int) -> Iterator[Dict]:
    """Query all team names in a season.

    Args:
        season: tournament year

    Returns:
        team 

    """
    teamsfile = os.path.join(DATA_PATH, 'original', 'Teams.csv')
    teams = pd.read_csv(teamsfile)

    for i, team in teams[(teams['FirstD1Season'] <= season) & (teams['LastD1Season'] >= season)].iterrows():
        yield team.to_dict()


def get_team_stats(season: int, team_id: int) -> Dict:
    """Query stats from team from specified season.

    Args:
        season:  year that a tournament took place
        team_id: unique identifier for a team

    Returns:
        series of team stats
    """
    statsfile = os.path.join(DATA_PATH, 'intermediate', 'base_team_stats.csv')
    stats = pd.read_csv(statsfile)

    return stats[(stats['kaggle_id'] == team_id) & (stats['season'] == season)].iloc[0].to_dict()
