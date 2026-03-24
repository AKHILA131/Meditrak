
from src.data_preprocessing import load_and_merge_data
from src.feature_engineering import create_features
from src.train_model import train_model
from src.predict import generate_future_predictions
from src.visualize import generate_visualizations

def main():
    print("Starting Meditrak Demand Forecasting Pipeline...\n")

    data = load_and_merge_data()
    data = create_features(data)
    model = train_model(data)
    generate_future_predictions()
    generate_visualizations(data)

    print("\nPreprocessing Completed Successfully!")
    print("\nFeature Engineering Completed Successfully!")
    print("\nModel Training Pipeline Completed Successfully!")
    print("\nFull Pipeline Completed Successfully!")
    print("\nFull Pipeline Completed Successfully!")

if __name__ == "__main__":
    main()

