import pandas as pd
import os
import matplotlib.pyplot as plt
import joblib
import numpy as np


def generate_visualizations(data):
    print("Generating Visualizations...")

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Create plots folder
    plots_path = os.path.join(project_root, "reports", "plots")
    os.makedirs(plots_path, exist_ok=True)

    # -----------------------------
    # 1. Actual vs Predicted Plot
    # -----------------------------
    model_path = os.path.join(project_root, "models", "best_model.pkl")
    model = joblib.load(model_path)

    temp_data = data.copy()

    # Drop date for prediction
    X = temp_data.drop(columns=["units_sold", "date"])
    y = temp_data["units_sold"]

    predictions = model.predict(X)

    plt.figure(figsize=(10, 5))
    plt.plot(y.values[:200], label="Actual")
    plt.plot(predictions[:200], label="Predicted")
    plt.legend()
    plt.title("Actual vs Predicted Demand")
    plt.savefig(os.path.join(plots_path, "actual_vs_predicted.png"))
    plt.close()

    print("Saved: actual_vs_predicted.png")

    # -----------------------------
    # 2. Monthly Sales Trend
    # -----------------------------
    temp_data["date"] = pd.to_datetime(temp_data["date"])

    monthly_sales = temp_data.groupby(temp_data["date"].dt.to_period("M"))["units_sold"].sum()

    plt.figure(figsize=(10, 5))
    monthly_sales.plot()
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.savefig(os.path.join(plots_path, "monthly_sales_trend.png"))
    plt.close()

    print("Saved: monthly_sales_trend.png")

    print("All visualizations generated successfully.")