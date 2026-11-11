import numpy as np
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).resolve().parent / "transactions.csv"


def preprocess_data():

    print("\n========== DATA PREPROCESSING ==========")

    data = pd.read_csv(DATA_PATH)

    print("\nOriginal dataset:")
    print(data.head())

    print("\nMissing values:")
    print(data.isnull().sum())

    # Remove duplicates
    data = data.drop_duplicates()

    # Replace infinite values
    data = data.replace(
        [np.inf, -np.inf],
        np.nan
    )

    # Remove rows with missing target
    data = data.dropna(subset=["is_fraud"])

    # Fill missing numerical values
    data = data.fillna(
        data.median(numeric_only=True)
    )

    # Separate features and target
    X = data.drop("is_fraud", axis=1)
    y = data["is_fraud"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("\nTraining data shape:", X_train.shape)
    print("Testing data shape:", X_test.shape)

    print("\nPreprocessing completed!")

    return {
        "data": data,
        "X": X,
        "y": y,
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test
    }


if __name__ == "main":
    preprocess_data()