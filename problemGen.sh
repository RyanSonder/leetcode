#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Error: No argument provided. You must specify a directory name."
  exit 1
fi


prob_path="src/problems/"
domain="https://leetcode.com/problems/${1//_/-}/"

# Create the Python file and initialize it with the class definition
PYTHON_FILE=$prob_path"$1.py"
cat <<EOL > "$PYTHON_FILE"
# $domain

class $1:

    def solution(self):
        ...
EOL


test_path="tests/problems/"
# Make blank unit tests
TEST_FILE=$test_path"test_$1.py"
cat <<EOL > "$TEST_FILE"
import pytest
from $1 import *

def test_solution():
    ...

EOL