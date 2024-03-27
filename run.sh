#!/bin/bash

cat banner.txt

python /module/crack.py

if [ $? -ne 0 ]; then
    echo "An error occurred while running the script..."
fi
