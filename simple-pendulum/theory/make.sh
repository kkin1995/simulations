#!/bin/bash

set -e
rm -f *.aux *.fdb_latexmk *.fls *.log *.gz
pdflatex simple-pendulum.tex
set +e