# Ryan Sonderman's Leetcode Solutions

This repository is for uploading and managing my LeetCode solutions. 

## Description

I have a script `problem_gen.py` that automatically creates a problem template given a problem name. When called, the script will generate a directory with a class, test, and readme template. 

Since I would like to focus on improving my Python right now, all solutions are done with Python3. 

The tests that are generated with `problem_gen.py` utilize benchmark to assess their speed. While I recognize the use of Big Oh runtime analysis, gains can also be had with small optimizations. Using the benchmarks, I try to optimize my solutions as much as possible. My goal is to come up with solutions that are efficient both in Big Oh running time, as well as practical running time. 

## Getting Started

### Dependencies

`pytest` is used to run unit tests on my solutions.

`pytest-benchmark` is used to analyze execution speed of my solutions.

### Installing

You can find the latest release on the [releases](https://github.com/RyanSonder/leetcode/releases) page.

Download and extract the contents of the zipped files.

### Executing the program

#### Generating a new problem template

While in the `leetcode` directory, run the generation script by typing `python3 problem_gen.py` in the terminal. The script will prompt you for the name of the problem and automatically generate a new directory in `src/problems/` containing the templates.

#### Coding your solutions

Unfortunately, I simply didn't have the time to code up a comprehensive Python IDE, so you will have to use your IDE of choice. I know, I'll try better in the future...

#### Running Tests

Once you have written a solution and entered the test cases, you can run a test by typing `pytest /src/problems/problem_name/` in the terminal. Alternatively, if you like waiting, you can just type `pytest` to run every single test case one after the other. Pytest will check accuracy and run benchmarks on the problems.

## Authors

Ryan Sonderman

@RyanSonder

e: ryansonderpersonal@gmail.com

---

Please contact me if you have any questions or changes you would like to see.

## Version History

* 1.0.0
* * Initial release launched with 13 completed problems

## License

MIT License

## Acknowledgements

* https://www.github.com