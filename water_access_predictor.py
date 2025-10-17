# water_access_predictor.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

from data_preprocessing import load_and_clean_data
from visualization import plot_feature_importance, plot_correlations


def main():
    # Load data
    df, encoders = load_and_clean_data('data.csv')

    # Define features and target
    X = df.drop(columns=['water_access_rate'])
    y = df['water_access_rate']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("Water Access Rate Model Results")
    print("--------------------------------")
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R² Score: {r2:.2f}")

    # Visualizations
    plot_feature_importance(model, X.columns)
    plot_correlations(df, 'water_access_rate')

    print("✅ Feature importance and correlation charts saved successfully.")


if __name__ == "__main__":
    main()
