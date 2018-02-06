#!/bin/bash

CWD=`pwd`
VISUALS_DIR="./visuals"
TEX_FILE=./latex/cs5720.tex
echo "\\documentclass{report}" > "$TEX_FILE"
echo "\\usepackage{minted}" >> "$TEX_FILE"
echo "\\usepackage{graphicx}" >> "$TEX_FILE"
echo "\\usepackage{verbatim}" >> "$TEX_FILE"
echo "\\begin{document}" >> "$TEX_FILE"
echo "    \\title{CS 5720: Data Visualization}" >> "$TEX_FILE"
echo "    \\maketitle" >> "$TEX_FILE"
for d in $VISUALS_DIR/* ; do
  DATA_PATH=`cat "$d/data_path"`
  OUTPUTS=`cat "$d/output_files"`
  echo "TEX_FILE=$TEX_FILE"
  echo "DATA_PATH=$DATA_PATH"
  echo "OUTPUTS=$OUTPUTS"
 
  echo "    \\chapter{${d//_/\\_}}" >> "$TEX_FILE"
  echo "    \\section{Description}" >> "$TEX_FILE"
  echo "    \\small" >> "$TEX_FILE"
  echo "    \\verbatiminput{../$d/README.md}" >> "$TEX_FILE"

  for script in `find "$d" -name "*.[Ss][Hh]"`; do
    DIR_NAME=`dirname $script`
    BASE_NAME=`basename $script`

    echo "    \\pagebreak" >> "$TEX_FILE"
    echo "    \\section{${DIR_NAME//_/\\_}}" >> "$TEX_FILE"

    for PYTHON_FILE in `find "$DIR_NAME" -name "*.[Pp][Yy]"`; do
      echo "    \\subsection{${PYTHON_FILE//_/\\_}}" >> "$TEX_FILE"
      echo "    \\inputminted{python}{../$PYTHON_FILE}" >> "$TEX_FILE"
    done
    for R_FILE in `find "$DIR_NAME" -name "*.[Rr]"`; do
      echo "    \\subsection{${R_FILE//_/\\_}}" >> "$TEX_FILE"
      echo "    \\inputminted{r}{../$R_FILE}" >> "$TEX_FILE"
    done
    for JAVA_FILE in `find "$DIR_NAME" -name "*.[Jj][Aa][Vv][Aa]"`; do
      echo "    \\subsection{${JAVA_FILE//_/\\_}}" >> "$TEX_FILE"
      echo "    \\inputminted{java}{../$JAVA_FILE}" >> "$TEX_FILE"
    done
    for C_FILE in `find "$DIR_NAME" -name "*.[CcHh]"`; do
      echo "    \\subsection{${C_FILE//_/\\_}}" >> "$TEX_FILE"
      echo "    \\inputminted{c}{../$C_FILE}" >> "$TEX_FILE"
    done
    for CPP_FILE in `find "$DIR_NAME" -name "*.[CcHh][Pp][Pp]"`; do
      echo "    \\subsection{${CPP_FILE//_/\\_}}" >> "$TEX_FILE"
      echo "    \\inputminted{cpp}{../$CPP_FILE}" >> "$TEX_FILE"
    done

    echo "$DIR_NAME"
    SKIP=1
    for OUTPUT in $OUTPUTS ; do
      OUTPUT_FILE="$DIR_NAME/$OUTPUT"
      echo "    \\subsection{${OUTPUT_FILE//_/\\_}}" >> "$TEX_FILE"
      echo "    \\includegraphics[width=\\textwidth]{../$OUTPUT_FILE}" >> "$TEX_FILE"
    done
  done
  echo "\\end{document}" >> "$TEX_FILE"
done
