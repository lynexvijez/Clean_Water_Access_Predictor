# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_importance(model, features, save_path='feature_importance.png'):
    """
    Plots feature importance for trained model.
    """
    importances = model.feature_importances_
    sorted_idx = importances.argsort()
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(importances)), importances[sorted_idx], color='skyblue')
    plt.yticks(range(len(features)), [features[i] for i in sorted_idx])
    plt.xlabel('Importance')
    plt.title('Feature Importance for Water Access Prediction')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_correlations(df, target_col='water_access_rate', save_path='correlation_heatmap.png'):
    """
    Plots correlation heatmap between numeric variables and water access rate.
    """
    numeric_df = df.select_dtypes(include=['number'])
    corr = numeric_df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=False, cmap='coolwarm')
    plt.title(f'Correlation Heatmap ({target_col})')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
