#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Error: No argument provided. You must specify a directory name."
  exit 1
fi


prob_path="src/problems/"
# Make problem directory within src/problems
mkdir $prob_path"$1"
touch $prob_path"$1"/README.md
touch $prob_path"$1"/"$1".py
touch $prob_path"$1"/__init__.py

test_path="tests/problems/"
# Make blank unit tests
touch $test_path"test_$1".py
echo "from $1 import *" >> $test_path"test_$1".py