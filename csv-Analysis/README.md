# Employee CSV Data Analysis

## 📌 Project Overview

Employee CSV Data Analysis is a Python-based data analysis project developed as part of the PugArch Technology 10-Day Technical Training Program.

The application reads employee records from a CSV file and generates useful statistical insights such as salary statistics, experience statistics, missing values, duplicate records, and department-wise analysis.

## 🎯 Objectives

* Read employee data from a CSV file
* Process and validate basic data types
* Calculate total employee records
* Analyze salary information
* Analyze employee experience
* Detect missing values
* Detect duplicate records
* Generate department-wise statistics
* Handle common file and data-processing errors
* Organize the program using reusable Python functions

## 🚀 Features

### 1. CSV Data Processing

Reads employee information using Python's built-in `csv` module.

### 2. Record Count

Displays the total number of employee records.

### 3. Salary Analysis

Calculates:

* Average salary
* Minimum salary
* Maximum salary

### 4. Experience Analysis

Calculates:

* Average experience
* Minimum experience
* Maximum experience

### 5. Missing Value Detection

Checks each CSV column for missing values.

### 6. Duplicate Detection

Identifies duplicate employee records.

### 7. Department-wise Statistics

Provides:

* Number of employees
* Average salary
* Minimum salary
* Maximum salary

for each department.

### 8. Exception Handling

Handles errors such as:

* Missing CSV file
* Invalid numeric data
* Unexpected processing errors

## 🛠️ Technologies Used

* Python 3
* CSV
* File Handling
* Lists
* Dictionaries
* Sets
* Functions
* List Comprehensions
* Exception Handling

## 📂 Project Structure

```text
csv-analysis/
│
├── data/
│   └── employees.csv
│
├── analysis.py
│
└── README.md
```

## ▶️ How to Run

### Step 1: Open the project folder

```bash
cd csv-analysis
```

### Step 2: Run the program

```bash
python analysis.py
```

## 📊 Sample Output

```text
============================================================
              EMPLOYEE CSV ANALYSIS
============================================================

Total Records: 12

Missing Values
------------------------------
employee_id: 0
name: 0
department: 0
salary: 0
experience: 0

Duplicate Records: 0

Salary Statistics
------------------------------
Average Salary: 64166.67
Minimum Salary: 50000.0
Maximum Salary: 80000.0

Experience Statistics
------------------------------
Average Experience: 3.92 years
Minimum Experience: 2.0 years
Maximum Experience: 7.0 years

Department Statistics
------------------------------
Department: IT
Employees: ...
Average Salary: ...
```

## 🧪 Testing

The project was tested for:

* Correct CSV file processing
* Missing values
* Duplicate records
* Invalid file path
* Numeric data conversion
* Department-wise calculations

## 📚 Learning Outcomes

Through this project, I practiced Python programming concepts including file handling, CSV processing, lists, dictionaries, sets, loops, functions, list comprehensions, data processing, statistics, and exception handling.

## 👩‍💻 Author

Name=Vaibhavi Mehar 
Year=4th Year 
Branch=Information Technology
