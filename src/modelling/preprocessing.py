import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df: pd.DataFrame):
    """
    Preprocess the dataset by one-hot encoding the 'Sex' column,
    scaling the features, and separating the target variable.

    Args:
        df (pd.DataFrame): The input DataFrame containing the dataset.

    Returns:
        tuple: X_scaled (scaled features), y (target),
        scaler (fitted scaler object)
    """
    # One-hot encode the 'Sex' column and separate target 'Rings'
    df = pd.get_dummies(df, columns=["Sex"], drop_first=True)
    X = df.drop(columns=["Rings"])
    y = df["Rings"]
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, scaler