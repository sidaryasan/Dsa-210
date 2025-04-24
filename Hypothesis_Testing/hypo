import pandas as pd
import re
from scipy.stats import ttest_ind
from datetime import datetime

# --- Helper Function: Extract date and calorie value from XML-like lines ---
def extract_calories(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        records = []
        for line in f:
            date_match = re.search(r'startDate="(\d{4}-\d{2}-\d{2})', line)
            value_match = re.search(r'value="([\d.]+)"', line)
            if date_match and value_match:
                date = pd.to_datetime(date_match.group(1))
                value = float(value_match.group(1))
                records.append((date, value))
        return pd.DataFrame(records, columns=["date", "calories"])

# --- Data Preparation ---
df = extract_calories("HKQuantityTypeIdentifierActiveEnergyBurned.txt")
df = df.groupby("date").sum().reset_index()

# --- Marking Lecture Days (Example: weekdays as lecture days) ---
lecture_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
df["weekday"] = df["date"].dt.day_name()
df["is_lecture_day"] = df["weekday"].isin(lecture_days)

# --- Hypothesis Test ---
lecture = df[df["is_lecture_day"]]["calories"]
non_lecture = df[~df["is_lecture_day"]]["calories"]
t_stat, p_val = ttest_ind(lecture, non_lecture, equal_var=False)

# --- Output ---
alpha = 0.05
if p_val < alpha:
    print("✅ Reject H0: Statistically significant difference in calorie burn between lecture and non-lecture days.")
else:
    print("❌ Fail to reject H0: No statistically significant difference in calorie burn between lecture and non-lecture days.")
print(f"T-statistic: {t_stat:.2f}, P-value: {p_val:.4f}")
