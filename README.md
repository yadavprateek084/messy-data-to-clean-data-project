# 🧹 Messy Data to Clean Data | Data Cleaning & Preprocessing Project

## 📌 Overview

This project demonstrates how messy, inconsistent real-world data can be transformed into a clean, structured dataset using Python.

It covers practical data cleaning techniques such as handling missing values, fixing inconsistent formats, removing outliers, and preparing data for analysis or machine learning workflows.

---

## 🎯 Project Objective

To simulate real-world data cleaning challenges and demonstrate hands-on skills in preparing raw datasets for data analysis.

---

## 🚀 Key Features

* Handling missing values using `fillna()` and `dropna()`
* Detecting and treating outliers
* Cleaning messy text and numerical data
* Extracting values using Regular Expressions (`re`)
* Converting incorrect data types
* Basic Exploratory Data Analysis (EDA)
* Data visualization using `matplotlib`

---

## 🧠 Skills Demonstrated

* Data Cleaning & Wrangling
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Regex-based Data Extraction
* Handling Missing Data & Outliers

---

## 🛠️ Tech Stack

* Python 🐍
* pandas
* numpy
* matplotlib
* regex (`re`)

---

## 📂 Project Structure

```
messy-data-to-clean-data/
│
├── data/
│   └── raw_data.csv
│
├── notebook/
│   └── data_cleaning.ipynb
│
├── output/
│   └── cleaned_data.csv
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/messy-data-to-clean-data.git
cd messy-data-to-clean-data
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
jupyter notebook
```

Open:

```
notebook/data_cleaning.ipynb
```

---

## 🔍 Sample Work (Before vs After Cleaning)

### 📌 Example 1: Extracting Age from Messy Data

**Before:**

```python
df['Age'] = ['23 years', 'Age: 45', 'Thirty', None]
```

**Cleaning Code:**

```python
import re

def extract_age(age):
    age_num = re.findall('[0-9]+', str(age))
    return int(age_num[0]) if age_num else None

df['Age'] = df['Age'].apply(extract_age)
```

**After:**

```
[23, 45, None, None]
```

---

### 📌 Example 2: Handling Missing Values

**Before:**

```python
df['Salary'].isnull().sum()
```

**Cleaning Code:**

```python
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
```

---

### 📌 Example 3: Removing Outliers

**Cleaning Code (IQR Method):**

```python
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Salary'] >= Q1 - 1.5 * IQR) & 
        (df['Salary'] <= Q3 + 1.5 * IQR)]
```

---

## 🔍 Before vs After Summary

* Fixed inconsistent formats (text → numeric)
* Handled missing values efficiently
* Removed extreme outliers
* Standardized categorical values
* Improved overall data quality

✅ Final Result: Clean, structured, analysis-ready dataset

---

## 📈 Output

```
output/cleaned_data.csv
```

---

## 💡 Future Improvements

* Build automated data cleaning pipeline
* Integrate with machine learning workflow
* Add dashboards for visualization
* Deploy as a web-based tool

---

## 📌 Use Case

This project is useful for:

* Data Analyst beginners
* Data Science learners
* Anyone working with messy real-world datasets

---

## 🙌 Author

**Prateek Yadav**
B.Tech CSE | Aspiring Data Analyst

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
