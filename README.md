# 📊 Analysis of Calorie Burn and Sleep Quality on Lecture Days

## 🧠 Motivation
Since I started attending classes at Sabancı University, I think my **calorie burn increases** and my **sleep patterns are affected** on lecture days because I commute to campus and follow a more structured schedule. This project is my way of investigating how much my class schedule actually affects my daily **physical activity and recovery** by analyzing the data I collect.

---

## 📦 Data Source
I'll be using my own fitness data collected through the Health app on my **smartphone and smartwatch**, which records various health metrics daily. For this project, I will focus on:
- **Active energy burned (calories)**
- **Sleep activity (duration and quality)**
- **Heart Rate**
The data will be exported in **XML format**.I changed format to **.txt**. I will process and filter the data to extract relevant records and match these records with my **lecture schedule(.json)**, which I extracted from the university’s academic calendar.

---

## 🔬 Data Analysis

### 📥 Data Collection and Cleaning
I'll export my health data into structured formats and clean it by aligning each day's calorie and sleep records with my lecture schedule, covering the period from **September 2024 to April 2025**.

### 📊 Exploratory Data Analysis (EDA)
I'll use visuals like **histograms**, **boxplots**, and **time series charts** to examine how daily **calorie burn**, **heart rates** and **sleep duration/quality** differ between lecture and non-lecture days.

### 🧪 Hypothesis Testing
I'll perform **t-tests** to determine whether the differences in **calorie burn**, **heart rates** and **sleep duration/quality** between lecture days and non-lecture days are statistically significant.


---

## 🔍 Findings

From this project, I want to find out:

- Do I burn significantly more calories on days I have lectures?
- Is there a noticeable difference in my sleep duration or quality between lecture and non-lecture days?
- How strongly does my class schedule influence my daily physical recovery and activity?
- Can health data like calories burned and sleep quality be used to accurately predict lecture days?

---

## ⚠️ Limitations and 🔮 Future Work

### Limitations
My data is limited by the accuracy of the smartphone and smartwatch sensors, the relatively short time period of data collection, and the lack of contextual variables like weather, stress, or external activities.

### Future Work
In future studies, I’d like to:
- Collect data over a longer period
- Integrate more metrics (e.g., heart rate, mood, steps)
- Explore correlations between academic stress and recovery metrics such as sleep
