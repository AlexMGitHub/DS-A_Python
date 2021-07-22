# Data Structures & Algorithms in Python

<p align="center">
<img src="docs/img/dsa_python_logo.png" title="Data Structures & Algorithms in Python" alt="Data Structures & Algorithms in Python" width="600"/>
</p>

## Overview

This repo contains solutions to selected exercises from the text [Data Structures and Algorithms in Python](https://www.wiley.com/en-us/Data+Structures+and+Algorithms+in+Python-p-9781118290279) by Goodrich, Tamassia, and Goldwasser.  All solutions are unit tested using [pytest](https://docs.pytest.org/en/6.2.x/contents.html) with 100% code [coverage](https://coverage.readthedocs.io/en/coverage-5.5/index.html).

I wrote the code in Python 3.9 and used `pytest` with the [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) plugin to test my solutions and check code coverage.  The repo is structured as a simple Python package that can be installed in editable mode using `pip`.  A **requirements.txt** file is included for convenience.

## DS-A_Python Contents

The DS-A_Python package has a standard directory structure with source code contained in the `src/` directory and unit tests contained in the `tests/` directory.  Some other files of interest include:

- **pytest.ini:** Settings for `pytest`.  I registered markers to ensure that typos in the marker names don't cause issues.
- **pylint.rc:** Settings for `pylint`.  I added a number of exceptions so that `pylint` doesn't ding my code for things like variable names (specified by the textbook) that violate the snake_case style.
- **gitignore:** Ignore HTML generated by pytest-cov, as well as various files generated by VS Code and egg files generated from installing the `dsa` package.
- **setup.py:** Needed to install local package `dsa`.

The `src/` directory contains three directories.  The solutions to the exercises are contained within `dsa/`, while some source code from the [textbook's GitHub repo](https://github.com/mjwestcott/Goodrich) (with license) is contained in the `textbook_src/` directory.  The third directory, `interviews/` consists of solutions to interview questions or exercises relevant to data structures and algorithms.

## Testing with `pytest`
`pytest` comes out of the box with powerful and easy-to-use features like test parameterization and test fixtures.  It also requires less boilerplate code than the `unittest` unit testing framework included in the Python standard library.  My secondary goal for working through *Data Structures and Algorithms in Python* was to become more familiar with`pytest`and software testing in general.  I learned how to parameterize tests, create my own custom test fixtures, mock Python built-ins, and use`pytest` plugins like `pytest-cov` to measure the code coverage of my tests.


### `pytest-cov`
I measured the code coverage of my Python source code using a `pytest`plugin called `pytest-cov`.  This plugin allows the user to generate code coverage reports directly from `pytest`.

The results from `pytest-cov` can be printed to the terminal, or saved to HTML and viewed in a web browser.  An example image of the HTML generated after a `pytest-cov` run is shown below:

<p align="center">
<img src="docs/img/coverage.png" title="Code coverage" alt="Code coverage" width="600"/>
</p>

I prefer to view the results in the web browser, as the source code for each tested file can be viewed by clicking on the link in the report.  All untested statements in the code are highlighted in red and easy to locate.


### Useful `pytest` Commands and Syntax

The following is a brief overview of the commands and syntax that I used most often when writing the unit tests in this repo.  Statements preceded by `$` indicate terminal commands; all other statements are Python code unless specified otherwise.

- Run all tests in package in verbose mode

`$ pytest -v`

- Run all tests in a module in verbose mode

`$ pytest -v tests/unit/test_chapter4.py`

- Run a specific test and disable stdout capture so that you can view print statements

`$ pytest -v -s tests/unit/test_chapter4.py::test_os_walk`

- Decorator to mark tests you'd like to skip

`@pytest.mark.skip(reason='Work in progress')`

- View list of registered markers

`$ pytest --markers`

- Run tests with strict markers option to catch marker typos

`$ pytest -v --strict-markers tests/unit/test_chapter4.py`

- Register markers in pytest.ini file for strict marker mode

```
[pytest]
markers =
    slow: Tests that are slow to execute.
```

- Don't run slow tests marked "slow"

`$ pytest -v --strict-markers -m 'not slow' tests/unit/test_chapter4.py`

#### Checking coverage:

- Run coverage over entire source directory, including source code that no tests have been written for

`$ pytest --cov=src`

- Run coverage over entire source directory and save report to HTML

`$ pytest --cov=src --cov-report=html`

- Tell pytest-cov to focus only on code tested by the `tests/` directory in the `dsa` package

`$ pytest --cov=dsa tests/ --cov-report=html`
