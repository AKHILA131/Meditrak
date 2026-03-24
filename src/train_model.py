import pandas as pd
import os
import joblib
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def train_model(data):
    print("Starting Model Training & Benchmarking...")

    # Drop date column
    data = data.drop(columns=["date"])

    # Features and target
    X = data.drop("units_sold", axis=1)
    y = data["units_sold"]

    # Time-based split (80-20)
    split_index = int(len(data) * 0.8)

    X_train = X[:split_index]
    X_test = X[split_index:]
    y_train = y[:split_index]
    y_test = y[split_index:]

    print("Data split into train and test sets.")

    # -----------------------
    # Model 1: Linear Regression
    # -----------------------
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.predict(X_test)

    lr_mae = mean_absolute_error(y_test, lr_pred)
    lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
    lr_r2 = r2_score(y_test, lr_pred)

    # -----------------------
    # Model 2: Random Forest
    # -----------------------
    rf_model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)

    rf_mae = mean_absolute_error(y_test, rf_pred)
    rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
    rf_r2 = r2_score(y_test, rf_pred)

    # -----------------------
    # Create Evaluation Report
    # -----------------------
    results = pd.DataFrame({
        "Model": ["Linear Regression", "Random Forest"],
        "MAE": [lr_mae, rf_mae],
        "RMSE": [lr_rmse, rf_rmse],
        "R2 Score": [lr_r2, rf_r2]
    })

    print("\nModel Evaluation Results:")
    print(results)

    # Select best model based on RMSE
    if rf_rmse < lr_rmse:
        best_model = rf_model
        best_model_name = "Random Forest"
    else:
        best_model = lr_model
        best_model_name = "Linear Regression"

    print(f"\nBest Model Selected: {best_model_name}")

    # Save best model
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    model_path = os.path.join(project_root, "models", "best_model.pkl")
    joblib.dump(best_model, model_path)

    # Save evaluation report
    report_path = os.path.join(project_root, "reports", "model_evaluation.csv")
    results.to_csv(report_path, index=False)

    print("Best model saved to models/best_model.pkl")
    print("Evaluation report saved to reports/model_evaluation.csv")

    return best_model