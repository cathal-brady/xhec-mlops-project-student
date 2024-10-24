# Abalone Age Prediction - MLOps Project

## 1. Project Context

The Abalone age prediction model aims to predict the age of abalone based on physical measurements. This project involves the industrialization of the Abalone age prediction model, ensuring that the model can be trained, retrained, and deployed in a production environment using modern MLOps practices such as workflow automation, version control, and CI/CD.

The goal is to build a robust pipeline for:
- Training the machine learning model.
- Making predictions on new data.
- Retraining the model on a regular schedule.
- Exposing the model via an API for real-time predictions.

The following sections outline how to set up the environment and run the code necessary to reproduce the entire pipeline.

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
