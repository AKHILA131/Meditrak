import pandas as pd
import os


def create_features(data):
    print("Starting Feature Engineering...")

    # Date-based features
    data["year"] = data["date"].dt.year
    data["month"] = data["date"].dt.month
    data["day"] = data["date"].dt.day
    data["day_of_week"] = data["date"].dt.dayofweek
    data["week_of_year"] = data["date"].dt.isocalendar().week

    print("Date features created.")

    # Weekend feature (if not already)
    data["is_weekend"] = data["day_of_week"].apply(lambda x: 1 if x >= 5 else 0)

    # Encode categorical variable
    data = pd.get_dummies(data, columns=["category"], drop_first=True)

    print("Categorical encoding completed.")

    # Save updated dataset
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    feature_path = os.path.join(project_root, "data", "processed", "featured_data.csv")
    data.to_csv(feature_path, index=False)

    print("Feature engineered data saved to data/processed/featured_data.csv")

    return data