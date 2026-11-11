from generatedata import generate_database
from processing import preprocess_data

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


def initialize():

    # 1. Generate dataset
    print("\n========== DATASET GENERATION ==========")

    generate_database()

    # 2. Process dataset
    processed = preprocess_data()

    data = processed["data"]
    X = processed["X"]
    y = processed["y"]

    X_train = processed["X_train"]
    X_test = processed["X_test"]

    y_train = processed["y_train"]
    y_test = processed["y_test"]

    # 3. Logistic Regression
    lr = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        ))
    ])

    # 4. Random Forest
    rf = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            class_weight="balanced"
        ))
    ])

    # 5. Train models
    print("\n========== MODEL TRAINING ==========")

    lr.fit(X_train, y_train)
    rf.fit(X_train, y_train)

    print("Both models trained successfully!")

    # 6. Predictions
    lr_pred = lr.predict(X_test)
    rf_pred = rf.predict(X_test)

    # 7. Evaluation
    def evaluate(actual, predicted):

        return {
            "accuracy": accuracy_score(actual, predicted),

            "precision": precision_score(
                actual, predicted,
                zero_division=0
            ),

            "recall": recall_score(
                actual, predicted,
                zero_division=0
            ),

            "f1": f1_score(
                actual, predicted,
                zero_division=0
            ),

            "confusion_matrix": confusion_matrix(
                actual, predicted
            )
        }

    lr_metrics = evaluate(y_test, lr_pred)
    rf_metrics = evaluate(y_test, rf_pred)

    # 8. Select best model
    if rf_metrics["f1"] >= lr_metrics["f1"]:

        best_model = rf
        best_model_name = "Random Forest"

    else:

        best_model = lr
        best_model_name = "Logistic Regression"

    print("\n========== MODEL RESULTS ==========")

    print("\nLogistic Regression:", lr_metrics)
    print("\nRandom Forest:", rf_metrics)

    print("\nSelected Model:", best_model_name)

    # 9. Return results
    return {
        "data": data,
        "X": X,
        "y": y,

        "X_train": X_train,
        "X_test": X_test,

        "lr": lr,
        "rf": rf,

        "lr_pred": lr_pred,
        "rf_pred": rf_pred,

        "y_test": y_test,

        "lr_metrics": lr_metrics,
        "rf_metrics": rf_metrics,

        "best_model": best_model,
        "best_model_name": best_model_name
    }


if __name__ == "__main__":
    initialize()