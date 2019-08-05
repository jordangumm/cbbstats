import os

from pathlib import Path

DATA_PATH = Path(os.path.dirname(os.path.realpath(__file__))) / 'data'

if not DATA_PATH.exists():
    DATA_PATH.mkdir()
