# Abalone Age Prediction - MLOps Project

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
conda activate abalone-mlops
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

### 1. Train the model

To train the model using Prefect, follow these steps after :

```bash
cd src/modelling
python main.py
```

This will download the data from Kaggle, preprocess it, train the model using the Ridge regression algorithm, and save the model and the scaler for future predictions.

### 2. Schedule Regular Retraining with Prefect
We have set up a Prefect deployment to retrain the model regularly. To start the worker that will handle the scheduled retraining jobs:

**How to run the prefect deployment**

1. Start the Prefect Worker:
    Open a new terminal and run:

    ```bash
    prefect worker start --pool 'MLOps'
    ```

    This worker will pick up scheduled jobs for model retraining.

2. Run the Prefect UI:
    To monitor flow runs, visualize tasks, and check logs, you can start the Prefect UI:

    ```bash
    prefect orion start
    ```

    Then, open your browser and go to http://127.0.0.1:4200 to see the Prefect dashboard.
    (Port 4200 has been used)

3. Trigger a Manual Run (Optional):
    To manually trigger a flow run for retraining, use the following command:

    ```bash
    prefect deployment run 'main/default'
    ```

    This command will execute the retraining flow immediately.

---

## Additional notes

- If any dependencies are updated in the requirements.in or requirements-dev.in files, make sure to regenerate their associated .txt files using pip-compile:

```bash
pip-compile requirements.in
pip-compile requirements-dev.in
```

- You can monitor the flow executions, schedules, and deployments through the Prefect UI as mentioned above.
- To redeploy the model or make updates, you can use the deployment configuration saved in the prefect.yaml file for faster deployments

```bash
prefect deploy -n default
```

## 4. Our FastAPI
Integrate Prefect with FastAPI to orchestrate and manage workflows triggered by HTTP requests for efficient data processing and task automation.
