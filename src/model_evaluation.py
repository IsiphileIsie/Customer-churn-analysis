from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)


def generate_predictions(model, X_test):
    """
    Generate class predictions and churn probabilities.

    Parameters:
        model: Trained classification model.
        X_test: Preprocessed testing features.

    Returns:
        y_pred: Predicted class labels.
        y_prob: Predicted probabilities for the churn class.
    """
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    return y_pred, y_prob


def calculate_metrics(y_test, y_pred, y_prob):
    """
    Calculate classification performance metrics.

    Parameters:
        y_test: Actual target labels.
        y_pred: Predicted target labels.
        y_prob: Predicted probabilities for customer churn.

    Returns:
        Dictionary containing classification metrics.
    """
    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, pos_label="Yes"),
        "Recall": recall_score(y_test, y_pred, pos_label="Yes"),
        "F1-score": f1_score(y_test, y_pred, pos_label="Yes"),
        "ROC-AUC": roc_auc_score(
            (y_test == "Yes").astype(int),
            y_prob
        )
    }

    return metrics


def calculate_confusion_matrix(y_test, y_pred):
    """
    Generate a confusion matrix.

    Parameters:
        y_test: Actual target labels.
        y_pred: Predicted target labels.

    Returns:
        A confusion matrix.
    """
    cm = confusion_matrix(
        y_test,
        y_pred,
        labels=["No", "Yes"]
    )

    return cm

def generate_classification_report(y_test, y_pred):
    """
    Generate a detailed classification report.

    Parameters:
        y_test: Actual target labels.
        y_pred: Predicted target labels.

    Returns:
        A classification report as a dictionary.
    """
    report = classification_report(
        y_test,
        y_pred,
        output_dict=True
    )

    return report