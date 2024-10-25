# Leetcode Solutions

This is the repo where I track the code used for my completed LeetCode questions.

In the main directory, I have a bash script called problemGen.sh, which automatically generates a subdirectory in src containing skeletons of the source code, test code, and readme.

## Source code

Each problem is completed using Python3, generally with as few external methods as possible.

## Testing

I always use the test cases provided by LeetCode, but I often add my own tests to cover edge cases and forse a worst-case running time. I use pytest-benchmark to generate mean runtimes for the solutions. With the mean runtimes, I will tweak the solution until I am happy with the efficiency.

If pytest is not installed: ```pip install pytest```

If benchmark is not installed: ```pip install pytest-benchmark```

## Readme

The readmes for each individual problem contains several bits of information. Primarily, it contains the problem description and my solution explanation. Secondarily, it contains my estimated running time in O-notation, the LeetCode running time in ms, and the LeetCode memory usage in MB.