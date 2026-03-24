import pandas as pd
import numpy as np
import os

np.random.seed(42)

# Get project root
project_root = os.path.abspath(os.path.dirname(__file__))
raw_path = os.path.join(project_root, "data", "raw")

# Ensure raw folder exists
os.makedirs(raw_path, exist_ok=True)

# Date range
dates = pd.date_range(start='2023-01-01', end='2023-12-31')

store_ids = [1, 2, 3, 4, 5]
item_ids = list(range(1001, 1021))

# -------- SALES DATA --------
sales_data = []

for date in dates:
    for store in store_ids:
        for item in item_ids:
            demand = np.random.poisson(lam=15)

            if date.month in [11, 12, 1, 2]:
                demand += 10

            if date.weekday() >= 5:
                demand += 5

            sales_data.append([date, store, item, demand])

sales = pd.DataFrame(sales_data, columns=["date", "store_id", "item_id", "units_sold"])
sales.to_csv(os.path.join(raw_path, "sales.csv"), index=False)

# -------- CALENDAR DATA --------
calendar = pd.DataFrame()
calendar["date"] = dates
calendar["day_of_week"] = calendar["date"].dt.dayofweek
calendar["is_weekend"] = calendar["day_of_week"].apply(lambda x: 1 if x >= 5 else 0)
calendar["is_holiday"] = np.random.choice([0, 1], size=len(calendar), p=[0.9, 0.1])
calendar["is_promo"] = np.random.choice([0, 1], size=len(calendar), p=[0.85, 0.15])
calendar.to_csv(os.path.join(raw_path, "calendar.csv"), index=False)

# -------- ITEM DATA --------
categories = ["Antibiotic", "Painkiller", "Vitamin", "Diabetes", "Cardiac"]

items = pd.DataFrame({
    "item_id": item_ids,
    "category": np.random.choice(categories, size=20),
    "base_price": np.random.uniform(50, 500, size=20).round(2)
})
items.to_csv(os.path.join(raw_path, "items.csv"), index=False)

print("✅ Data successfully generated inside data/raw/")