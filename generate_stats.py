"""Generate base stats.


"""


import os, sys
import pkg_resources

import click
import numpy  as np
import pandas as pd

from tqdm import tqdm

from cbbstats.pathutil import DATA_PATH


def get_minutes_played(team_wins, team_losses):
    """ Calculate minutes a team played """
    mp = (len(team_wins) * 40) + (team_wins['NumOT'].sum() * 5)
    mp += (len(team_losses) * 40) + (team_losses['NumOT'].sum() * 5)
    return mp


def get_base_team_stats(team_wins, team_losses):
    """ Return combined per minute stat differentials for team
    Arguments:
    team_wins - pandas DataFrame of won games for team in season
    team_losses - pandas DataFrame of lost games for team in season
    """
    def get_team_stat(team_wins, team_losses, stat):
        """ Return sum of specified team stat """
        return team_wins['W{}'.format(stat)].sum() + team_losses['L{}'.format(stat)].sum()

    def get_opp_stat(team_wins, team_losses, stat):
        """ Return sum of specified stat of opponents of team played """
        return team_wins['L{}'.format(stat)].sum() + team_losses['W{}'.format(stat)].sum()

    output = {}

    for stat in team_wins.keys():
        if stat[0] != 'W' or 'Team' in stat or 'Loc' in stat: continue
        stat = stat[1:]
        output['{}'.format(stat)] = float(get_team_stat(team_wins,team_losses,stat))
        output['opp_{}'.format(stat)] = float(get_opp_stat(team_wins,team_losses,stat))
    return output


def get_four_factors(stats: pd.DataFrame) -> pd.DataFrame:
    """Calculate Dean Oliver's Four Factors of Basketball Success.

    1. Shooting
        - effective field goal percentage (eFG%)
    2. Turnovers
        - turnover percentage (TOV%)
    3. Rebounding
        - offensive rebound percentage (ORB%)
        - defensive rebound percentage (DRB%)
    4. Free Throws
        - free throw rate (FTR)

    Args:
        team_stats: dataframe of base team statistics

    Returns:
        Original dataframe with Four Factor columns added.

    """
    stats['eFG%'] = (stats['FGM'] + 0.5 * stats['FGM3']) / stats['FGA']
    stats['opp_eFG%'] = (stats['opp_FGM'] + 0.5 * stats['opp_FGM3']) / stats['opp_FGA']

    stats['TO%'] = stats['TO'] / (stats['FGA'] + 0.44 * stats['FTA'])
    stats['opp_TO%'] = stats['opp_TO'] / (stats['opp_FGA'] + 0.44 * stats['opp_FTA'])

    stats['OR%'] = stats['OR'] / (stats['OR'] + stats['opp_DR'])
    stats['DR%'] = stats['DR'] / (stats['opp_OR'] + stats['DR'])

    stats['FTR'] = stats['FTA'] / stats['FGA']
    stats['opp_FTR'] = stats['opp_FTA'] / stats['opp_FGA']

    return stats


def generate_base_stats(games_df, teams_df, output_fp):
    """ Summed stats for every team in every year

    """
    output = None
    for i, season in enumerate(tqdm(range(games_df['Season'].min(),games_df['Season'].max()+1))):
        season_games = games_df[games_df['Season'] == season]
        teams = set(season_games['WTeamID'].unique().tolist() + season_games['LTeamID'].unique().tolist())

        for k, team in enumerate(tqdm(teams)):
            team_wins = season_games[season_games['WTeamID'] == team]
            team_losses = season_games[season_games['LTeamID'] == team]

            team_stats = get_base_team_stats(team_wins, team_losses)
            team_stats = get_four_factors(team_stats)

            team_stats['kaggle_id'] = team
            team_stats['minutes_played'] = get_minutes_played(team_wins, team_losses)
            team_stats['team_name'] = teams_df[teams_df['TeamID'] == team]['TeamName'].unique()[0]
            team_stats['season'] = season

            team_stats['winning_pct'] = float(len(team_wins)) / float(len(team_wins) + len(team_losses))

            if type(output) == type(None):
                output = pd.DataFrame(team_stats, index=[i + (len(season_games)*i) + k])
            else:
                output = output.append(pd.DataFrame(team_stats, index=[i + (len(season_games)*i) + k]))

    output.to_csv(output_fp, index=None)


def run():
    """Coordinate creation of base team stats CSV file."""
    games  = pd.read_csv(os.path.join(DATA_PATH, 'original', 'MDataFiles_Stage1', 'MRegularSeasonDetailedResults.csv'))
    teams  = pd.read_csv(os.path.join(DATA_PATH, 'original', 'MDataFiles_Stage1', 'MTeams.csv'))
    output = os.path.join(DATA_PATH, 'intermediate')

    if not os.path.exists(output):
        os.makedirs(output)
        
    print(f'writing to {output}')
    generate_base_stats(games, teams, os.path.join(output, 'team_stats.csv'))


if __name__ == "__main__":
    run()
