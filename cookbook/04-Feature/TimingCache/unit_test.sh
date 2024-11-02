#!/bin/bash

set -e
set -x
#clear

python3 main.py > log-main.py.log

if [ $TRT_COOKBOOK_CLEAN ]; then
    rm -rf *.TimingCache *.log
fi

echo "Finish `basename $(pwd)`"
