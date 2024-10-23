#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Error: No argument provided. You must specify a directory name."
  exit 1
fi

path="src/problems/$1"
mkdir "$path"
domain="https://leetcode.com/problems/${1//_/-}/"

# Make python file
PYTHON_FILE=$path/"$1.py"
cat <<EOL > "$PYTHON_FILE"
# $domain

class $1:

    def solution():
        ...
EOL

# Make unit test
TEST_FILE=$path/"test_$1.py"
cat <<EOL > "$TEST_FILE"
import pytest
from $1 import *

def test_not_implemented():
    assert False

EOL

# Make README.md
README_FILE=$path/"README.md"
cat <<EOL > "$README_FILE"
# Problem: $1

## Question:

Not yet documented.

## Solution:

Not yet documented.


EOL