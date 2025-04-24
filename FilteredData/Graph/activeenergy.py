import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt

# --- 1. Read and process calorie data from Apple Health export ---
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

# --- 2. Load the data and compute daily totals ---
df = extract_calories("HKQuantityTypeIdentifierActiveEnergyBurned.txt")
df = df.groupby("date").sum().reset_index()
df["weekday"] = df["date"].dt.day_name()

# --- 3. Calculate average calories burned for each weekday ---
weekly_avg = df.groupby("weekday")["calories"].mean()

# --- 4. Ensure weekdays are in calendar order ---
ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekly_avg = weekly_avg.reindex(ordered_days)

# --- 5. Plot the bar chart ---
plt.figure(figsize=(8, 5))
weekly_avg.plot(kind="bar", color="mediumturquoise")
plt.title("Average Calories Burned by Day of the Week")
plt.xlabel("Weekday")
plt.ylabel("Average Calories Burned")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("weekly_calorie_averages.png", dpi=300)
plt.show()
