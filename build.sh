#!/bin/bash

DATADIR=$1

echo "$DATADIR" > "$DATADIR"

mkdir -p "$DATADIR"
kaggle competitions download -c mens-machine-learning-competition-2018
unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/DataFiles.zip -d "$DATADIR/original/"
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/MasseyOrdinals_thruSeason2018_Day128 -d mcbb/data/original/
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/PlayByPlay_2010.zip -d mcbb/data/original/play_by_play
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/PlayByPlay_2011.zip -d mcbb/data/original/play_by_play
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/PlayByPlay_2012.zip -d mcbb/data/original/play_by_play
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/PlayByPlay_2013.zip -d mcbb/data/original/play_by_play
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/PlayByPlay_2014.zip -d mcbb/data/original/play_by_play
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/PlayByPlay_2015.zip -d mcbb/data/original/play_by_play
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/PlayByPlay_2016.zip -d mcbb/data/original/play_by_play
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/PlayByPlay_2017.zip -d mcbb/data/original/play_by_play
#unzip ~/.kaggle/competitions/mens-machine-learning-competition-2018/PlayByPlay_2018.zip -d mcbb/data/original/play_by_play

