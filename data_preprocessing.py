# data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_clean_data(file_path):
    """
    Loads and cleans dataset for the water access model.
    """
    df = pd.read_csv(file_path)

    # Drop duplicates and missing values
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Encode categorical columns
    label_encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    return df, label_encoders
