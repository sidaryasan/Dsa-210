# 📊 How Do Lecture Days Affect My Daily Physical Activity?

## 🧠 Motivation
Since I began attending classes at Sabancı University, I’ve noticed that my physical activity tends to fluctuate depending on whether I have lectures that day. This project explores **how lecture days influence my overall daily activity**, with a focus on **sleep patterns** as a measurable output of physical demand and routine disruption. The idea is to see if attending classes significantly impacts how much I rest and recover.

---

## 📦 Data Source

The data used in this project comes from two personal devices:
- **Smartphone**: Collecting general health and lifestyle metrics
- **Smartwatch**: Providing more precise and continuous sleep tracking data

Data is exported from the Apple Health app in XML format and processed using custom-built tools. I extracted **sleep activity data** (`HKCategoryTypeIdentifierSleepAnalysis`) and aligned it with my **lecture schedule**, retrieved from the university's academic calendar.

---

## 🧪 Data Analysis

The following steps are applied to examine the relationship between lecture days and sleep activity:

### 🔹 Data Collection & Cleaning
- Filtered and parsed the XML export from Apple Health to extract daily sleep data
- Converted class schedule (from university portal) into structured JSON
- Mapped each date as either a **"lecture day"** or **"non-lecture day"**

### 🔹 Exploratory Data Analysis (EDA)
- Created **histograms**, **boxplots**, and **line plots** to observe trends in sleep duration
- Compared general sleep patterns between days with and without lectures

### 🔹 Hypothesis Testing
- Applied **independent t-tests** to assess whether the differences in average sleep durations between lecture and non-lecture days are statistically significant

### 🔹 Machine Learning (To Be Implemented)
- Planned implementation of a classification model (e.g., logistic regression) to predict whether a day is a lecture day based on sleep data alone

---

## 📈 Key Questions

- Do I sleep less or more on days I attend university lectures?
- Is there a measurable difference in the **quality or quantity** of sleep between these two types of days?
- Can sleep data be used to **predict academic workload or physical demands**?
- Does attending classes disrupt or improve my overall rest pattern?

---

## 🚧 Limitations and Future Work

### ⚠️ Limitations
- Sleep data accuracy can vary between smartphone and smartwatch sensors
- The observation window is limited to September 2024 – April 2025
- No external factors (e.g., exam weeks, health conditions) are currently factored in

### 🔮 Future Work
- Include longer-term data across multiple semesters
- Incorporate additional metrics like **calories burned**, **heart rate**, and **mood tracking**
- Investigate correlations between academic stress and sleep quality

---

## 🧰 Tech Stack

- **Language**: Python (required)
- **Libraries**: pandas, matplotlib, scipy
- **IDE**: Jupyter Notebook / VS Code / PyCharm
- **Data Format**: Apple Health XML → parsed to CSV / DataFrame

---

## 📝 Submission Info

- All code and analysis will be submitted via GitHub as per course requirements
- A `requirements.txt` file and detailed documentation will be included
- Regular commits will be made to document project progress

---

> This project is conducted as part of the **DSA 210: Introduction to Data Science** course at Sabancı University – 2024-2025 Spring Term.
