import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_churn_distribution(df):
    """
    Plot the distribution of customers who churned and stayed.

    Parameters:
        df: Customer DataFrame containing the Churn column.
    """
    plt.figure(figsize=(8, 5))

    sns.countplot(data=df, x="Churn")

    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")

    plt.tight_layout()
    plt.show()

def plot_numerical_distributions(df, numerical_features):
    """
    Plot the distributions of numerical customer features.

    Parameters:
        df: Customer DataFrame.
        numerical_features: List of numerical column names.
    """
    for feature in numerical_features:
        plt.figure(figsize=(8, 5))

        sns.histplot(data=df, x=feature, kde=True)

        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")

        plt.tight_layout()
        plt.show()

def plot_categorical_distributions(df, categorical_features):
    """
    Plot the distributions of categorical customer features.

    Parameters:
        df: Customer DataFrame.
        categorical_features: List of categorical column names.
    """
    for feature in categorical_features:
        plt.figure(figsize=(9, 5))

        sns.countplot(
            data=df,
            x=feature,
            hue=feature,
            order=df[feature].value_counts().index,
            legend=False
        )

        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Number of Customers")
        plt.xticks(rotation=45, ha="right")

        plt.tight_layout()
        plt.show()

def plot_churn_rate(df, categorical_features):
    """
    Plot customer churn rates across categorical features.

    Parameters:
        df: Customer DataFrame.
        categorical_features: List of categorical column names.
    """
    for feature in categorical_features:
        churn_rates = (
            df.groupby(feature)["Churn"]
            .apply(lambda x: (x == "Yes").mean() * 100)
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(9, 5))

        sns.barplot(
            x=churn_rates.index,
            y=churn_rates.values
        )

        plt.title(f"Churn Rate by {feature}")
        plt.xlabel(feature)
        plt.ylabel("Churn Rate (%)")
        plt.xticks(rotation=45, ha="right")

        plt.tight_layout()
        plt.show()


def plot_numerical_features_by_churn(df, numerical_features):
    """
    Compare numerical customer features across churn groups.

    Parameters:
        df: Customer DataFrame.
        numerical_features: List of numerical column names.
    """
    for feature in numerical_features:
        plt.figure(figsize=(8, 5))

        sns.boxplot(data=df, x="Churn", y=feature)

        plt.title(f"{feature} by Customer Churn")
        plt.xlabel("Churn")
        plt.ylabel(feature)

        plt.tight_layout()
        plt.show()
