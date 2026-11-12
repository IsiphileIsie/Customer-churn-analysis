import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def separate_features_target(df):
    """
    Separate the customer features from the churn target.

    Parameters:
        df: Cleaned customer DataFrame.

    Returns:
        X: Predictor variables.
        y: Target variable.
    """
    X = df.drop(columns=["Churn", "customerID"])
    y = df["Churn"]

    return X, y

def identify_feature_types(X):
    """
    Identify numerical and categorical features.

    Parameters:
        X: DataFrame containing predictor variables.

    Returns:
        numerical_features: List of numerical column names.
        categorical_features: List of categorical column names.
    """
    numerical_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object"]
    ).columns.tolist()

    return numerical_features, categorical_features

def split_data(X, y):
    """
    Split the dataset into training and testing sets.

    Parameters:
        X: Predictor variables.
        y: Target variable.

    Returns:
        X_train, X_test, y_train, y_test.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test

def create_preprocessor(numerical_features, categorical_features):
    """
    Create a preprocessing pipeline for numerical and categorical features.

    Parameters:
        numerical_features: List of numerical column names.
        categorical_features: List of categorical column names.

    Returns:
        A fitted-independent ColumnTransformer.
    """
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ]
    )

    return preprocessor

def preprocess_data(preprocessor, X_train, X_test):
    """
    Fit the preprocessor on training data and transform both datasets.

    Parameters:
        preprocessor: ColumnTransformer object.
        X_train: Training predictor variables.
        X_test: Testing predictor variables.

    Returns:
        X_train_processed, X_test_processed.
    """
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    return X_train_processed, X_test_processed