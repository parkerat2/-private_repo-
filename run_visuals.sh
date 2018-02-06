#!/bin/bash

CWD=`pwd`
VISUALS_DIR="./visuals"
for d in $VISUALS_DIR/* ; do
  DATA_PATH=`cat "$d/data_path"`
  OUTPUTS=`cat "$d/output_files"`
  echo "DATA_PATH=$DATA_PATH"
  echo "OUTPUTS=$OUTPUTS"
  for script in `find "$d" -name "*.[Ss][Hh]"`; do
    DIR_NAME=`dirname $script`
    BASE_NAME=`basename $script`
    echo "$DIR_NAME"
    cd "$DIR_NAME"
    SKIP=1
    for OUTPUT in $OUTPUTS ; do
      if [ ! -f $OUTPUT ] ; then
        echo "$OUTPUT not found."
        SKIP=0
      fi
    done
    if [ "$SKIP" -eq "1" ] ; then
      echo "Skipping..."
    else
      echo bash -r "$BASE_NAME" "$DATA_PATH" $OUTPUTS
      bash -r "$BASE_NAME" "$DATA_PATH" $OUTPUTS
    fi
    cd "$CWD"
  done
done
