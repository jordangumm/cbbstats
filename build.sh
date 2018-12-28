#!/bin/bash

set -e

DATADIR=$1

mkdir -p "$DATADIR/original/play_by_play"
kaggle competitions download -c mens-machine-learning-competition-2018 -p "$DATADIR/compressed"

unzip "$DATADIR/compressed/DataFiles.zip" -d "$DATADIR/original/"
unzip "$DATADIR/compressed/MasseyOrdinals_thruSeason2018_Day128.zip" -d "$DATADIR/original/"
unzip "$DATADIR/compressed/PlayByPlay_2010.zip" -d "$DATADIR/original/play_by_play"
unzip "$DATADIR/compressed/PlayByPlay_2011.zip" -d "$DATADIR/original/play_by_play"
unzip "$DATADIR/compressed/PlayByPlay_2012.zip" -d "$DATADIR/original/play_by_play"
unzip "$DATADIR/compressed/PlayByPlay_2013.zip" -d "$DATADIR/original/play_by_play"
unzip "$DATADIR/compressed/PlayByPlay_2014.zip" -d "$DATADIR/original/play_by_play"
unzip "$DATADIR/compressed/PlayByPlay_2015.zip" -d "$DATADIR/original/play_by_play"
unzip "$DATADIR/compressed/PlayByPlay_2016.zip" -d "$DATADIR/original/play_by_play"
unzip "$DATADIR/compressed/PlayByPlay_2017.zip" -d "$DATADIR/original/play_by_play"
unzip "$DATADIR/compressed/PlayByPlay_2018.zip" -d "$DATADIR/original/play_by_play"
