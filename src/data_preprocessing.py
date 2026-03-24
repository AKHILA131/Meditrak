import pandas as pd
import os


def load_and_merge_data():
    print("Loading datasets...")

    # Get project root directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Construct file paths
    sales_path = os.path.join(project_root, "data", "raw", "sales.csv")
    calendar_path = os.path.join(project_root, "data", "raw", "calendar.csv")
    items_path = os.path.join(project_root, "data", "raw", "items.csv")

    print("Sales path:", sales_path)

    # Load CSV files
    sales = pd.read_csv(sales_path)
    calendar = pd.read_csv(calendar_path)
    items = pd.read_csv(items_path)

    print("Datasets loaded successfully.")

    # Convert date columns
    sales["date"] = pd.to_datetime(sales["date"])
    calendar["date"] = pd.to_datetime(calendar["date"])

    # Merge datasets
    print("Merging datasets...")
    data = sales.merge(calendar, on="date", how="left")
    data = data.merge(items, on="item_id", how="left")

    print("Merging completed.")

    # Handle missing values
    print("Handling missing values...")
    data.fillna(0, inplace=True)

    # Save processed data
    processed_path = os.path.join(project_root, "data", "processed", "merged_data.csv")
    data.to_csv(processed_path, index=False)

    print("Preprocessed data saved to data/processed/merged_data.csv")

    return data