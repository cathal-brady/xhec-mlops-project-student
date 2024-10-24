import pickle

import mlflow


def save_model(model, model_name):
    """
    Save the model to MLflow.
    Args:
        model: The trained model object.
        model_name (str): The name of the model to be saved.
    """
    mlflow.sklearn.log_model(model, model_name)


def load_model(model_name):
    """
    Load the model from MLflow.
    Args:
        model_name (str): The name of the model to be loaded.
    Returns:
        model: The loaded model.
    """
    model_uri = f"models:/{model_name}/latest"
    return mlflow.sklearn.load_model(model_uri)


def save_object(obj, filename):
    """
    Save an object like a scaler to a file using pickle.
    Args:
        obj: The object to be saved.
        filename (str): The name of the file to save the object.
    """
    with open(filename, "wb") as f:
        pickle.dump(obj, f)


def load_object(filename):
    """
    Load an object from a file using pickle.
    Args:
        filename (str): The name of the file to load the object from.
    Returns:
        object: The loaded object.
    """
    with open(filename, "rb") as f:
        return pickle.load(f)
