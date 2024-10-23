#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Error: No argument provided. You must specify a directory name."
  exit 1
fi

# Proceed with the script if $1 exists
cd src || exit
mkdir "$1"
cd "$1" || exit
touch README.md
touch "$1.py"