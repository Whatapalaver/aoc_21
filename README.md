# Advent of Code Python Starter

A template for [Advent of Code](https://adventofcode.com) written in Python. The original repo by [ljgago](https://github.com/ljgago/advent-of-code-python-starter) I have just amended so that I can run in a Docker container and therefore avoid venv setup issues but also switched to having one solution file per day - to save repitition.

## Usage

### When running from the terminal with Docker

To generate your container and open the terminal run `make run`

Commands can then be run directly from this prompt:

- Generate file structure `python -m aoc.gen day01`
- To test day01 `pytest tests/test_day01.py`
- To run your output `python -m aoc.day01`

## Config

You can configure the automatic input download from the Advent of Code
session token.

To dowload the inputs from AOC website, you need to set the environment var `AOC_SESSION`. 
You can to get the session token from the cookie web browser.

Also can you set the `AOC_YEAR` to select a certain year.
(It is not mandatory use the `AOC_YEAR`, aoc.gen can get the year automatically)

You can set an `.env` file with these variables.

Folder structure:

    ├── aoc
    │   └── day01
    │       ├── __main__.py
    │       ├── solution.py
    │       ├── README.md
    │       └── resources
    │           └── input.txt
    └── tests
        ├── conftest.py
        └── test_day01.py

Happy coding!

[MIT License](LICENSE)
