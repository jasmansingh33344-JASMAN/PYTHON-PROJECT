import numpy as np
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "transactions.csv"


def generate_database():



    n = 10000

    amount = np.random.randint(100, 100000, n)
    hour = np.random.randint(0, 24, n)
    account_age = np.random.randint(1, 2000, n)
    transactions = np.random.randint(1, 15, n)
    distance = np.random.randint(1, 1000, n)
    international = np.random.randint(0, 2, n)
    failed_pin = np.random.randint(0, 5, n)
    device_changed = np.random.randint(0, 2, n)

    fraud_score = (
        (amount > 70000).astype(int) +
        (hour <= 4).astype(int) +
        (distance > 300).astype(int) +
        international +
        (failed_pin >= 2).astype(int) +
        device_changed
    )

    is_fraud = (fraud_score >= 3).astype(int)

    data = pd.DataFrame({
        "amount": amount,
        "hour": hour,
        "account_age": account_age,
        "transactions": transactions,
        "distance": distance,
        "international": international,
        "failed_pin": failed_pin,
        "device_changed": device_changed,
        "is_fraud": is_fraud
    })

    data.to_csv(DATA_PATH, index=False)

    print("\nDataset generated successfully!")
    print("Total transactions:", len(data))
    print("\nFraud distribution:")
    print(data["is_fraud"].value_counts())

    return data


if __name__ == "main":
    generate_database()