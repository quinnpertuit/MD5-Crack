#!/bin/bash

cat banner.txt

cd module
python /module/crack.py

if [ $? -ne 0 ]; then
    echo "An error occurred while running the script..."
fi
