# 📊 Analysis of Step Count and Sleep Duration Patterns

## 🧠 Motivation
I wanted to investigate how my physical activity (measured by step count) correlates with my sleep patterns, and whether there are predictable patterns in my weekly activity levels. This project analyzes my health data to better understand the relationship between daily activity and sleep habits.

## 📦 Data Source
I used my own fitness data collected through the Health app on my smartphone and smartwatch, which records various health metrics daily. For this project, I focused on:
- **Daily step count**
- **Sleep duration**
- **Bedtime hours**

The data was exported in XML format and processed to extract relevant metrics.

## 🔬 Data Analysis

### 📥 Data Preparation
I exported my health data and converted it to a structured format for analysis. The process involved:
1. Extracting records from Apple Health export.xml
2. Creating daily summaries for step count and sleep duration
3. Merging these datasets for combined analysis

### 📊 Exploratory Data Analysis (EDA)
I created various visualizations to explore:
- Daily step count patterns
- Sleep duration distribution
- Day of week comparisons
- Monthly trends

### 🧪 Hypothesis Testing
I conducted three main hypothesis tests:

1. **Step Count vs. Sleep Duration**
  - Tested for correlation between daily step count and sleep duration
  - Used Pearson correlation analysis

2. **Day of Week Effect on Step Count**
  - Tested whether certain days of the week show different activity levels
  - Used ANOVA to compare step counts across days

3. **Bedtime Impact on Next Day's Activity**
  - Attempted to analyze whether bedtime affects next day's step count
  - Used correlation analysis to test this relationship

### 🤖 Machine Learning Analysis
I applied two basic machine learning models to further explore patterns:

1. **Random Forest**: Predicting sleep duration from step count
  - R² Score: -0.03
  - RMSE: 1.15 hours

2. **Decision Tree**: Analyzing day of week patterns in step count
  - R² Score: -0.02
  - RMSE: 3733.78 steps

## 🔍 Key Findings

1. **Steps & Sleep Relationship**:
  - No significant correlation was found between daily step count and sleep duration
  - The machine learning model confirmed this with a negative R² score, indicating step count is not a useful predictor for sleep duration

2. **Weekly Activity Patterns**:
  - No consistent pattern in step count across different days of the week
  - The Decision Tree model failed to find predictable patterns based on day of week

3. **Bedtime Impact Analysis**:
  - No significant correlation was found between bedtime hour and next day's step count
  - This suggests that sleep timing does not significantly influence next day's activity level

Unlike my original plan that focused on lecture days versus non-lecture days and calorie burn, this analysis took a broader approach to explore general patterns in my health data without specific context to academic schedules.

## ⚠️ Limitations and 🔮 Future Work

### Limitations
- Limited health metrics - analysis focused mainly on step count rather than comprehensive activity metrics like calorie burn
- Missing contextual information (weather, events, stress levels)
- Inconsistent bedtime data limited certain analyses
- Relatively short time period of data collection

### Future Work
For future analysis, I would like to:
- Collect more consistent bedtime and sleep quality data
- Track additional metrics (heart rate, stress levels, calorie burn)
- Include contextual data (lecture days, weather, mood)
- Apply more advanced time series analysis methods
- Investigate specific periods (exam weeks, holidays) for pattern changes

As initially planned in my previous approach, I still hope to eventually analyze the impact of academic schedules on my health patterns when more comprehensive data becomes available.
