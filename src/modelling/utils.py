import pickle
import mlflow

def save_model(model, model_name, file_path='src/web_service/local_objects'):
    """
    Save the model to MLflow and also as a pickle file in the specified file path.
    Args:
        model: The trained model object.
        model_name (str): The name of the model to be saved.
        file_path (str): The local directory where the model will be saved.
    """
    # Log the model with MLflow
    mlflow.sklearn.log_model(model, model_name)

    # Save the model as a pickle file in the local_objects folder
    with open(f'{file_path}/{model_name}.pkl', 'wb') as f:
        pickle.dump(model, f)


def load_model(model_name, file_path='src/web_service/local_objects'):
    """
    Load the model from a pickle file in the specified file path.
    Args:
        model_name (str): The name of the model to be loaded.
        file_path (str): The local directory where the model is saved.
    Returns:
        model: The loaded model.
    """
    # Load the model from a pickle file
    with open(f'{file_path}/{model_name}.pkl', 'rb') as f:
        return pickle.load(f)


def save_object(obj, filename, file_path='src/web_service/local_objects'):
    """
    Save an object like a scaler to a file using pickle.
    
    Args:
        obj: The object to be saved.
        filename (str): The name of the file to save the object.
        file_path (str): The local directory where the object will be saved.
    """
    with open(f'{file_path}/{filename}', "wb") as f:
        pickle.dump(obj, f)


def load_object(filename, file_path='src/web_service/local_objects'):
    """
    Load an object from a file using pickle.
    
    Args:
        filename (str): The name of the file to load the object from.
        file_path (str): The local directory where the object is saved.
    Returns:
        object: The loaded object.
    """
    with open(f'{file_path}/{filename}', "rb") as f:
        return pickle.load(f)
