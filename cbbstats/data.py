import os
import pkg_resources

import pandas as pd

from cbbstats.pathutil import DATA_PATH


def load_teams():
    return pd.read_csv(os.path.join(DATA_PATH, 'original', 'Teams.csv'))


def load_tournament_teams():
    return pd.read_csv(os.path.join(DATA_PATH, 'original', 'NCAATourneySeeds.csv'))


def load_team_stats():
    return pd.read_csv(os.path.join(DATA_PATH, 'intermediate', 'team_stats.csv'))


def load_team_seeds():
    return pd.read_csv(os.path.join(DATA_PATH, 'original', 'NCAATourneySeeds.csv'))


def load_team_rankings(system='POM', daynum=133):
    df = pd.read_csv(os.path.join(DATA_PATH, 'original', 'MasseyOrdinals.csv'))
    print(df.keys())
    df = df.loc[df['SystemName'] == system]
    df = df.loc[df['RankingDayNum'] == daynum]
    return df
