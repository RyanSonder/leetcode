#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Error: No argument provided. You must specify a directory name."
  exit 1
fi


prob_path="src/problems/"
# Make problem directory within src/problems
touch $prob_path"$1".py

test_path="tests/problems/"
# Make blank unit tests
touch $test_path"test_$1".py
echo "from $1 import *" >> $test_path"test_$1".py