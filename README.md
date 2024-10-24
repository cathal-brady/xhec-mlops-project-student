<<<<<<< HEAD
<div align="center">

# xhec-mlops-project-student

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)
</div>

This repository has for purpose to industrialize the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest.

<details>
<summary>Details on the Abalone Dataset</summary>

The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.

**Goal**: predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc...)

You can download the dataset on the [Kaggle page](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset)

</details>
=======
# Abalone Age Prediction - MLOps Project
>>>>>>> f4f1029428dd2a4e1bd2a385820527d6f55f2aea

## Table of Contents
1. [Project Context](#1-project-context)
2. [Participants](#2-participants)
3. [Steps to Recreate the Python Environment](#3-steps-to-recreate-the-python-environment)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#1-clone-the-repository)
    - [Set Up the Virtual Environment](#2-set-up-the-virtual-environment)
    - [Install Dependencies](#3-install-dependencies)
    - [Set Up Pre-commit Hooks](#4-set-up-pre-commit-hooks)
4. [Instructions to Run the Code](#4-instructions-to-run-the-code)
5. [Additional Notes](#additional-notes)

## 1. Project Context

This is a group project for MLOps class based on [this repository](https://github.com/artefactory/xhec-mlops-project-student) and [this Kaggle challenge](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset). The objective of this repository is the industrialization of an Abalone Age Prediction model(please find data on Kaggle).

The Abalone age prediction involves predicting the age of abalone based on physical measurements such as shell weight, diameter, and others. The actual age of an abalone is determined by counting rings on its shell, a tedious and time-consuming process. The model's goal is to replace this manual task by predicting the "Rings" column using other available measurements.

This repository contains all the components required to automate the machine learning pipeline for training, inference, and deployment of the Abalone age prediction model.

### Key Features of the Repository:
- **Model Training and Inference Workflow**: We use Prefect to manage the workflows for both training the model and making predictions. The workflows are modularized into separate tasks and flows, making it easier to manage and maintain.
- **Automated Retraining**: A Prefect deployment is set up to regularly retrain the model, ensuring it stays up to date as new data becomes available.g
- **API Deployment**: The repository contains an API built using FastAPI that allows users to submit new data and receive real-time age predictions for abalone. The API is integrated with Pydantic for input validation.
- **Pre-commit Hooks for Code Quality**: The repository uses `black`, `isort`, and `ruff` to ensure clean, consistent code formatting and linting, enforced by pre-commit hooks.

### By following the instructions in this README, you'll be able to:
- **Recreate the development environment** used for the project.
- **Train and retrain the model using Prefect**.
- **Deploy an API** that serves predictions based on new input data.
- Ensure that the code adheres to the coding standards and practices set by the project.

---

## 2. Participants

- **Hadrien Strichard** - [hadrienstrichard](https://github.com/hadrienstrichard)
- **Hocine Zidi** - [Hozidi](https://github.com/Hozidi)
- **Jean-Eudes Agbre** - [JokyHub](https://github.com/JokyHub)
- **Tarek Massoud** - [tarekmassoud](https://github.com/tarekmassoud)
- **Cathal Brady** - [cathal-brady](https://github.com/cathal-brady)

---

## 3. Steps to Recreate the Python Environment

### Prerequisites

Ensure you have the following installed on your machine:

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/downloads/release/python-3110/)
[![Git](https://img.shields.io/badge/Git-Installed-green)](https://git-scm.com/downloads)

You'll also need either `virtualenv` or `conda` installed to create a virtual environment.

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/cathal-brady/xhec-mlops-project-student.git
cd xhec-mlops-project-student
```

### 2. Set Up the Virtual Environment

**Using Conda**

If you have Conda installed, you can use the environment.yml file to recreate the environment:

```bash
# Create the environment using conda
conda env create --file environment.yml

# Activate the environment
conda activate abaloneenv
```

**Using Virtualenv**

If you prefer using virtualenv, follow these steps:

```bash
# Install virtualenv if you don't have it already
pip install virtualenv

# Create the virtual environment
virtualenv abaloneenv --python=python3.11

# Activate the environment
source abaloneenv/bin/activate  # For MacOS/Linux
abaloneenv\Scripts\activate     # For Windows
```

### 3. Install dependencies

Once the environment is activated, install the dependencies:

```bash
pip install -r requirements.txt
```
If you need to install development tools like black, flake8, and isort, run:

```bash
pip install -r requirements-dev.txt
```

To ensure code quality and formatting before each commit, install the pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
```
This ensures that every time you make a commit, code formatters and linters (like black, isort, and flake8) will be applied automatically.

---

## 4. Instructions to Run the Code

---

## Additional notes

- If any dependencies are updated in the requirements.in or requirements-dev.in files, make sure to regenerate the .txt files using pip-compile:

```bash
pip-compile requirements.in
pip-compile requirements-dev.in
```

- If any dependencies are updated in the requirements.in or requirements-dev.in files, make sure to regenerate the .txt files using pip-compile:

```bash
pip-compile requirements.in
pip-compile requirements-dev.in
```
