"""Player Statistics

This module is dedicated to querying data and stats for players.

"""

import csv
import os
import pkg_resources

import pandas as pd

DATA_PATH = pkg_resources.resource_filename('cbbstats', 'data/')

for d in os.listdir(DATA_PATH):
    print(d)
