"""Generate player stats."""

import os
import pkg_resources

from os      import PathLike
from pathlib import Path

import pandas as pd

from tqdm import tqdm


DATA_PATH = pkg_resources.resource_filename('cbbstats', 'data')


def run() -> None:
    """Generage player stats based on play by play data."""
    play_by_play = Path(DATA_PATH + '/original/play_by_play')
    output = Path(DATA_PATH + '/intermediate')

    if not output.exists():
        os.makedirs(output)

    for season in tqdm(range(2010, 2020)):
        plays = pd.read_csv(play_by_play / f'Events_{season}.csv')
        players = pd.read_csv(play_by_play / f'Players_{season}.csv')

        print(plays)

if __name__ == '__main__':
    run()
