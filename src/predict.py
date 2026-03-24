import pandas as pd
import os
import joblib
import numpy as np


def generate_future_predictions():
    print("Starting Future Demand Prediction...")

    # Get project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Load trained model
    model_path = os.path.join(project_root, "models", "demand_model.pkl")
    model = joblib.load(model_path)

    # Load featured dataset
    data_path = os.path.join(project_root, "data", "processed", "featured_data.csv")
    data = pd.read_csv(data_path)

    # Use last 30 days as base for simulation
    future_data = data.tail(30).copy()

    # Drop target column
    X_future = future_data.drop(columns=["units_sold", "date"])

    # Predict
    predictions = model.predict(X_future)

    future_data["predicted_units"] = np.round(predictions)

    # Save predictions
    forecast_path = os.path.join(project_root, "reports", "next_month_forecast.csv")
    future_data.to_csv(forecast_path, index=False)

    print("Future forecast saved to reports/next_month_forecast.csv")

    return future_data

