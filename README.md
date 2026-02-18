# 🎓 Student Data Cleaning & Performance Analysis System

A Python-based data cleaning and analysis system designed to process student records, remove inconsistencies, and generate meaningful insights.

This project demonstrates core concepts of **data validation, duplicate removal, filtering, statistical analysis, and modular programming**.

---

## 🚀 Project Overview

The system processes raw student data that may contain:

- Duplicate records
- Invalid marks (negative or greater than 100)
- Missing values
- Unclean entries

It cleans the dataset and performs performance analysis.

---

## 📌 Features

### 🧹 Data Cleaning
- Remove duplicate student records (based on ID)
- Validate marks (only 0–100 allowed)
- Remove invalid entries
- Handle missing values

---

### 📊 Performance Analysis
- Assign grades automatically
- Calculate average marks
- Identify highest scoring student
- Identify lowest scoring student
- Display cleaned dataset

---

## 🏗 Project Structure

student_cleaning_project/
│
├── main.py
└── README.md

---

## 🛠 Technologies Used

- Python
- Lists
- Dictionaries
- Sets
- Functions
- Lambda expressions
- Basic statistical calculations

---

## 🧠 Concepts Implemented

- Data Validation
- Duplicate Detection using Set
- Conditional Filtering
- Modular Programming
- Statistical Aggregation
- Feature Engineering (Grade Assignment)

---

## 📂 Sample Data Structure

Each student record is stored as a dictionary:

```python
{
    "id": 1,
    "name": "Aman",
    "marks": 78
}
```
