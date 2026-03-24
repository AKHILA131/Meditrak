# Import required modules from src
from src.data_preprocessing import load_and_merge_data
from src.feature_engineering import create_features
from src.train_model import train_model
from src.predict import generate_future_predictions
from src.visualize import generate_visualizations


def main():

    # Pipeline Start
    print("🚀 Starting Meditrak Demand Forecasting Pipeline...\n")


    # Step 1: Data Preprocessing
    # print("📥 Running Data Preprocessing...")
    data = load_and_merge_data()
    print("✅ Preprocessing Completed Successfully!\n")


    # Step 2: Feature Engineering
    # print("🧠 Running Feature Engineering...")
    data = create_features(data)
    print("✅ Feature Engineering Completed Successfully!\n")


    # Step 3: Model Training & Evaluation
    # print("🤖 Running Model Training...")
    model = train_model(data)
    print("✅ Model Training Completed Successfully!\n")


    # Step 4: Future Demand Prediction
    # print("🔮 Generating Future Predictions...")
    generate_future_predictions()
    print("✅ Prediction Completed Successfully!\n")


    # Step 5: Visualization
    # print("📊 Generating Visualizations...")
    generate_visualizations(data)
    print("✅ Visualization Completed Successfully!\n")


    # Final Pipeline Status
    print(" Full Pipeline Completed Successfully!..✅✅")


# Entry point of the program
if __name__ == "__main__":
    main()

