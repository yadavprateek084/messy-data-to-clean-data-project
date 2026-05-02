import pandas as pd
import numpy as np
import random

n = 10000

# Base clean data
df = pd.DataFrame({
    "Customer_ID": [f"CUST{1000+i}" for i in range(n)],
    "Name": [f"Customer_{i}" for i in range(n)],
    "Gender": np.random.choice(['M','F'], n),
    "Age": np.random.randint(18, 70, n),
    "City": np.random.choice(['Delhi','Mumbai','Kolkata','Chennai','Hyderabad'], n),
    "Signup_Date": pd.date_range(start='2020-01-01', periods=n, freq='D'),
    "Last_Purchase_Date": pd.date_range(start='2021-01-01', periods=n, freq='D'),
    "Purchase_Amount": np.random.randint(1000,50000,n),
    "Feedback_Score": np.random.randint(1,11,n),
    "Email": [f"user{i}@example.com" for i in range(n)],
    "Phone_Number": np.random.randint(900000000,9999999999,n),
    "Country": "India"
})

# --- Inject REALISTIC MESSINESS ---

# 1. Age corruption (like "51 years")
idx = np.random.choice(n, 1000, replace=False)
df.loc[idx, "Age"] = df.loc[idx, "Age"].astype(str) + " years"

# 2. Gender inconsistency
df.loc[np.random.choice(n, 1500), "Gender"] = np.random.choice(
    ['male','female','m','f','FEMALE'], 1500
)

# 3. City casing issues
df.loc[np.random.choice(n, 2000), "City"] = df["City"].str.lower()
df.loc[np.random.choice(n, 1500), "City"] = df["City"].str.upper()

# 4. Missing values (controlled)
for col in ["Customer_ID","Gender","Age","City","Last_Purchase_Date","Purchase_Amount","Feedback_Score","Country"]:
    df.loc[np.random.choice(n, 1000, replace=False), col] = np.nan

# 5. Purchase outliers
df.loc[np.random.choice(n, 50), "Purchase_Amount"] = 9999999
df.loc[np.random.choice(n, 50), "Purchase_Amount"] = -500

# 6. Country inconsistency
df.loc[np.random.choice(n, 2000), "Country"] = "india"

# Save
df.to_csv("messy_customer_sales_data_FIXED.csv", index=False)

print("✅ High-quality messy dataset generated")
