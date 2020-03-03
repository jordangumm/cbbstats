set -e

BASE=$(readlink -f $0)
BASEDIR=`dirname $BASE`
DATADIR="$BASEDIR/cbbstats/data"

if [ ! -d "$DATADIR" ]; then
    kaggle competitions download -c google-cloud-ncaa-march-madness-2020-division-1-mens-tournament -p "$DATADIR/compressed"
    
    unzip "$DATADIR/compressed/google-cloud-ncaa-march-madness-2020-division-1-mens-tournament.zip" -d "$DATADIR/original/"
fi

python "$BASEDIR/generate_stats.py"
