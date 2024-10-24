# Setting up the virtual environment and installing dependencies

## Overview
This branch concerns building the virtual environment and installing dependencies, as well as ensuring later code will meet some code quality conventions.

## Prerequisites
To get started, you will need the following installed on your machine:

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/downloads/release/python-3110/)
[![Git](https://img.shields.io/badge/Git-Installed-green)](https://git-scm.com/downloads)

## Setup Instructions

### 1. Clone the Repository
Begin by cloning the repository to your local machine:

```bash
git clone https://github.com/cathal-brady/xhec-mlops-project-student.git
cd path/to/wherever/you/cloned/this/repo
```

### 2. Set up a virtual environment

We did this using virtualenv
If you dont have virtualenv you can install it as below
```bash
# Install virtualenv package
$ pip install virtualenv

# Create the virtual environment
$ virtualenv abaloneenv --python=python3.11
```

This is a virtual environment specifically for our abalone prediction

activate the environment using

<code>abaloneenv\Scripts\activate</code> (Windows)
<code>source abaloneenv/bin/activate</code> (on MacOS/Linux)

Install the dependencies we have laid out in the requirements file
<code>pip install -r requirements.txt</code>

Configure pre-commit hooks by running
pip install pre-commit
pre-commit install


This ensures All code in this repository must adhere to the following conventions:

    flake8: For linting and enforcing coding style.
    isort: For sorting imports to keep code organized.
    black: For automatic code formatting to maintain cons

Which are laid out in our requirements dev-in files (see <code>requirements-dev.in</code> for a summary)

By following these steps, you will have a well-configured development environment ready for contributing to this project. If you encounter any issues or have questions, please refer to the documentation for the respective tools or reach out for assistance.
