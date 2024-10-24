# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.

import argparse
from pathlib import Path
from training import flow

def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Trigger the Prefect flow to train the model
    flow.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)