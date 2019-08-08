"""Games

This module is dedictated to querying tournament games.

"""

import csv
import os
import pkg_resources

from typing import Iterator, Dict

import pandas as pd

from cbbstats.pathutil import DATA_PATH


def get_tournament_games(season: int, compact: bool = True) -> Iterator[Dict]:
    """Query played NCAA Tournament season games.

    Args:
        season: tournament year

    Return:
        tournament games

    """
    if compact:
        gamesfile = os.path.join(DATA_PATH, 'original', 'NCAATourneyCompactResults.csv')
    else:
        gamesfile = os.path.join(DATA_PATH, 'original', 'NCAATourneyDetailedResults.csv')

    games = pd.read_csv(gamesfile)
    for i, game in games[games['Season'] == season].iterrows():
        yield game.to_dict()


def get_regular_games(season: int, compact: bool = True) -> Iterator[Dict]:
    """ """
    if compact:
        gamesfile = os.path.join(DATA_PATH, 'original', 'RegularSeasonCompactResults.csv')
    else:
        gamesfile = os.path.join(DATA_PATH, 'original', 'RegularSeasonDetailedResults.csv')

    games = pd.read_csv(gamesfile)
    for i, game in games[games['Season'] == season].iterrows():
        yield game.to_dict()


def get_tournament_results(compact: bool = True) -> Iterator[Dict]:
    """Query played NCAA Tournament season games.

    Args:
        season: tournament year

    Return:
        tournament games

    """
    if compact:
        gamesfile = os.path.join(DATA_PATH, 'original', 'NCAATourneyCompactResults.csv')
    else:
        gamesfile = os.path.join(DATA_PATH, 'original', 'NCAATourneyDetailedResults.csv')

    return pd.read_csv(gamesfile)


def get_regular_results(compact: bool = True) -> Iterator[Dict]:
    """ """
    if compact:
        gamesfile = os.path.join(DATA_PATH, 'original', 'RegularSeasonCompactResults.csv')
    else:
        gamesfile = os.path.join(DATA_PATH, 'original', 'RegularSeasonDetailedResults.csv')

    return pd.read_csv(gamesfile)

