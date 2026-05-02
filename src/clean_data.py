import pandas as pd
import re

def extract_age(age):
    age_num = re.findall('[0-9]+', str(age))
    return int(age_num[0]) if age_num else None

def clean_data(df):
    # Clean Age column
    if 'Age' in df.columns:
        df['Age'] = df['Age'].apply(extract_age)

    # Handle missing values
    for col in df.select_dtypes(include=['float64', 'int64']):
        df[col] = df[col].fillna(df[col].median())

    # Remove outliers using IQR
    for col in df.select_dtypes(include=['float64', 'int64']):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        df = df[(df[col] >= Q1 - 1.5 * IQR) &
                (df[col] <= Q3 + 1.5 * IQR)]

    return df


if __name__ == "__main__":
    df = pd.read_csv("data/raw_data.csv")
    df_cleaned = clean_data(df)
    df_cleaned.to_csv("output/cleaned_data.csv", index=False)
    print("✅ Data cleaned and saved!")
