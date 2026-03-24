# 💊 Meditrak Demand Forecasting System

## 📌 Project Overview

This project is an end-to-end Machine Learning pipeline developed to forecast medicine demand across multiple pharmacy stores. It is designed as part of an academic internship and aims to enhance the Meditrak healthcare management system with predictive analytics.

The system helps optimize inventory, reduce wastage, and prevent stockouts by predicting future demand using historical sales data.

---

## 🎯 Business Objectives

- Optimize inventory levels across stores
- Reduce overstock and expired medicines
- Prevent stockouts of essential drugs
- Automate demand forecasting
- Identify seasonal demand trends

---

## 🏗️ Project Architecture

```
Raw Data → Preprocessing → Feature Engineering → Model Training → Evaluation → Prediction → Visualization
```


---

## 📂 Project Structure
```
meditrak-demand-forecasting/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── models/
│ └── best_model.pkl
│
├── reports/
│ ├── model_evaluation.csv
│ ├── next_month_forecast.csv
│ └── plots/
│
├── src/
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── train_model.py
│ ├── predict.py
│ └── visualize.py
│
├── main.py
├── generate_data.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

## 🔄 Workflow Explanation

### 1️⃣ Data Preprocessing
- Load sales, calendar, and item datasets
- Merge datasets
- Handle missing values
- Save cleaned dataset

### 2️⃣ Feature Engineering
- Extract date features (month, day, weekday)
- Create weekend indicators
- Encode categorical variables

### 3️⃣ Model Training & Benchmarking
- Models used:
  - Linear Regression (baseline)
  - Random Forest (advanced)
- Metrics used:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² Score

### 4️⃣ Model Selection
- Best model selected based on RMSE
- Random Forest performed better in this case

### 5️⃣ Demand Prediction
- Predict future demand using trained model
- Generate next month forecast

### 6️⃣ Visualization
- Actual vs Predicted graph
- Monthly sales trend analysis

---

## 📊 Model Performance

| Model              | MAE   | RMSE  | R² Score |
|--------------------|-------|-------|----------|
| Linear Regression  | 12.41 | 13.52 | -4.34    |
| Random Forest      | 8.59  | 9.67  | -1.73    |

✅ Random Forest selected as best model

---

## 📈 Key Insights

- Model captures overall demand trend effectively
- Seasonal demand observed during winter months
- Predictions are stable and consistent
- Suitable for inventory planning

---

## 🚀 How to Run the Project
-->bash terminal


### 1. Clone Repository

```git clone <your-repo-link>```

```cd meditrak-demand-forecasting```


### 2. Create Virtual Environment

```python -m venv venv```

```source venv/Scripts/activate```


### 3. Install Dependencies

```pip install -r requirements.txt```

### Add libraries and freeze the requirements and (Update pip if needed)

```pip install pandas numpy matplotlib seaborn scikit-learn```

```pip freeze > requirements.txt```

```python --version```


### 4. Run Pipeline
```python main.py```

---

📦 Outputs Generated
models/best_model.pkl → Trained model
reports/model_evaluation.csv → Model comparison
reports/next_month_forecast.csv → Future demand
reports/plots/ → Visualization graphs

---

🧠 Future Improvements
Use advanced models (XGBoost, LSTM)
Add real-time data integration
Deploy using Streamlit or Flask
Improve forecasting with time-series models

---

👩‍💻 Author 
- Akhila T
2003akhilat@gmail.com




