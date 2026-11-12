from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent


def load_raw_data(input_path):
    """
    Load the raw customer dataset.

    Parameters:
        input_path: Path to the raw CSV file.

    Returns:
        A pandas DataFrame containing the raw data.
    """
    df = pd.read_csv(input_path)

    return df


def clean_customer_data(df):
    """
    Clean the customer dataset.

    Replaces whitespace-only TotalCharges values with 0
    and converts the column to numeric.

    Parameters:
        df: Raw customer DataFrame.

    Returns:
        A cleaned DataFrame.
    """
    df_clean = df.copy()

    df_clean["TotalCharges"] = df_clean["TotalCharges"].replace(
        r"^\s*$", "0", regex=True
    )

    df_clean["TotalCharges"] = pd.to_numeric(
        df_clean["TotalCharges"]
    )

    return df_clean


def save_cleaned_data(df, output_path):
    """
    Save the cleaned customer dataset to a CSV file.

    Parameters:
        df: Cleaned customer DataFrame.
        output_path: Destination path for the cleaned CSV file.
    """
    df.to_csv(output_path, index=False)


def main():
    input_path = BASE_DIR / "data" / "raw" / "customer_raw_data.csv"
    output_path = BASE_DIR / "data" / "processed" / "customer_cleaned_data.csv"

    df = load_raw_data(input_path)

    df_clean = clean_customer_data(df)

    save_cleaned_data(df_clean, output_path)


if __name__ == "__main__":
    main()
