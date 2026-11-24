from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

def train_logistic_regression(X_train, y_train, class_weight=None):
    """
    Train a Logistic Regression model.

    Parameters:
        X_train: Preprocessed training features.
        y_train: Training target variable.
        class_weight: Class weighting strategy.

    Returns:
        A trained Logistic Regression model.
    """
    model = LogisticRegression(
        max_iter=1000,
        class_weight=class_weight,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def train_random_forest(X_train, y_train):
    """
    Train a Random Forest classification model.

    Parameters:
        X_train: Preprocessed training features.
        y_train: Training target variable.

    Returns:
        A trained Random Forest model.
    """
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def train_gradient_boosting(X_train, y_train):
    """
    Train a Gradient Boosting classification model.

    Parameters:
        X_train: Preprocessed training features.
        y_train: Training target variable.

    Returns:
        A trained Gradient Boosting model.
    """
    model = GradientBoostingClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model