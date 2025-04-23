# 📊 Project Title: How Do Lecture Days Affect My Daily Physical Activity?

## 🧠 Motivation
Since I began attending classes at Sabancı University, I have observed that my daily activity levels vary depending on whether I have lectures. On days with classes, I commute to campus, walk between buildings, and generally move more. This project aims to explore how my academic schedule influences my physical activity by analyzing my personal health data.

---

## 📦 Data Source
I will use my own fitness data, collected through the Health app on my **smartphone** and **smartwatch**. The dataset includes various metrics such as:

- **Active energy burned (calories)**
- **Sleep activity**
- **Heart rate**
- And more

For this project, I will primarily focus on **active energy burned** as an indicator of daily activity.

The data is exported in **XML format** and processed to extract relevant records. These records are then **cross-referenced with my lecture schedule**, which I manually extracted from the university academic calendar and formatted into structured JSON.

---

## 🔬 Data Analysis

To investigate the relationship between lecture days and activity, I will follow these steps:

### 1. Data Collection and Cleaning
- Filter the activity data to cover the period between **September 2024 and April 2025**.
- Label each date as either a **lecture day** or **non-lecture day** based on my course schedule.

### 2. Exploratory Data Analysis (EDA)
- Use visualization tools such as **histograms**, **boxplots**, and **time series plots** to examine how daily activity levels (in calories burned) differ between lecture and non-lecture days.

### 3. Hypothesis Testing
- Perform statistical analysis using a **t-test** to evaluate whether the difference in calorie burn between lecture and non-lecture days is statistically significant.

### 4. Machine Learning
- Attempt to build a basic **classification model** (e.g., logistic regression or decision tree) to predict whether a day was a lecture day using only activity metrics like calorie burn.

---

## 🔍 Findings

This project will help answer the following questions:

- Do I burn significantly more calories on days I have lectures?
- Is there a clear distributional difference in daily activity between lecture and non-lecture days?
- How strongly does my class schedule influence my physical movement?
- Can activity data alone predict whether I had classes?

---

## ⚠️ Limitations and 🔮 Future Work

### Limitations
- The data comes from **two devices (smartphone and smartwatch)** and may contain measurement errors.
- The study does not currently factor in **external variables** such as weather, academic workload, or emotional stress.

### Future Work
- Expand the dataset to cover **multiple academic terms** for stronger generalization.
- Incorporate additional activity metrics (e.g., **steps**, **heart rate**
