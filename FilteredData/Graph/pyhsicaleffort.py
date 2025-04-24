import pandas as pd
import re
import matplotlib.pyplot as plt

# 1. Extract daily physical effort data from Apple Health export
def extract_physical_effort(filepath):
    records = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if 'HKQuantityTypeIdentifierAppleExerciseTime' not in line:
                continue
            date_match = re.search(r'startDate="(\d{4}-\d{2}-\d{2})', line)
            value_match = re.search(r'value="([\d.]+)"', line)
            if date_match and value_match:
                date = pd.to_datetime(date_match.group(1))
                minutes = float(value_match.group(1))  # Already in minutes
                records.append((date, minutes))
    return pd.DataFrame(records, columns=["date", "exercise_minutes"])

# 2. Load and group data by date
df = extract_physical_effort("HKQuantityTypeIdentifierAppleExerciseTime.txt")
df = df.groupby("date").sum().reset_index()
df["weekday"] = df["date"].dt.day_name()

# 3. Order weekdays
ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df["weekday"] = pd.Categorical(df["weekday"], categories=ordered_days, ordered=True)

# 4. Plot boxplot
plt.figure(figsize=(10, 6))
df.boxplot(column="exercise_minutes", by="weekday", grid=False)
plt.title("Boxplot of Daily Physical Effort (Exercise Time) by Weekday")
plt.suptitle("")  # Remove auto title
plt.xlabel("Weekday")
plt.ylabel("Exercise Time (minutes)")
plt.tight_layout()
plt.savefig("physical_effort_boxplot.png", dpi=300)
plt.show()
