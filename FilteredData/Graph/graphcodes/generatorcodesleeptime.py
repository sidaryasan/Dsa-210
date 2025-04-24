import pandas as pd
import re
import matplotlib.pyplot as plt

# --- 1. Function to extract sleep records from Apple Health lines ---
def extract_sleep(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        records = []
        for line in f:
            if 'HKCategoryTypeIdentifierSleepAnalysis' not in line:
                continue
            start_match = re.search(r'startDate="(.*?)"', line)
            end_match = re.search(r'endDate="(.*?)"', line)
            if start_match and end_match:
                start = pd.to_datetime(start_match.group(1))
                end = pd.to_datetime(end_match.group(1))
                duration_hours = (end - start).total_seconds() / 3600  # convert duration to hours
                date = start.date()
                records.append((pd.to_datetime(date), duration_hours))
        return pd.DataFrame(records, columns=["date", "sleep_hours"])

# --- 2. Process sleep data: group by date and calculate total per day ---
df = extract_sleep("HKCategoryTypeIdentifierSleepAnalysis.txt")  # ← Change this to your file path
df = df.groupby("date").sum().reset_index()
df["weekday"] = df["date"].dt.day_name()

# --- 3. Calculate average sleep per weekday ---
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
avg_sleep = df.groupby("weekday")["sleep_hours"].mean().reindex(weekday_order)

# --- 4. Plot the line chart ---
plt.figure(figsize=(8, 5))
plt.plot(avg_sleep.index, avg_sleep.values, marker='o', linestyle='-', color='mediumpurple')
plt.title("Average Sleep Duration by Day of the Week")
plt.xlabel("Weekday")
plt.ylabel("Average Sleep Hours")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("average_sleep_line_plot.png", dpi=300)
plt.show()
import pandas as pd
import re
import matplotlib.pyplot as plt

# --- 1. Function to extract sleep records from Apple Health lines ---
def extract_sleep(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        records = []
        for line in f:
            if 'HKCategoryTypeIdentifierSleepAnalysis' not in line:
                continue
            start_match = re.search(r'startDate="(.*?)"', line)
            end_match = re.search(r'endDate="(.*?)"', line)
            if start_match and end_match:
                start = pd.to_datetime(start_match.group(1))
                end = pd.to_datetime(end_match.group(1))
                duration_hours = (end - start).total_seconds() / 3600  # convert duration to hours
                date = start.date()
                records.append((pd.to_datetime(date), duration_hours))
        return pd.DataFrame(records, columns=["date", "sleep_hours"])

# --- 2. Process sleep data: group by date and calculate total per day ---
df = extract_sleep("HKCategoryTypeIdentifierSleepAnalysis.txt")  # ← Change this to your file path
df = df.groupby("date").sum().reset_index()
df["weekday"] = df["date"].dt.day_name()

# --- 3. Calculate average sleep per weekday ---
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
avg_sleep = df.groupby("weekday")["sleep_hours"].mean().reindex(weekday_order)

# --- 4. Plot the line chart ---
plt.figure(figsize=(8, 5))
plt.plot(avg_sleep.index, avg_sleep.values, marker='o', linestyle='-', color='mediumpurple')
plt.title("Average Sleep Duration by Day of the Week")
plt.xlabel("Weekday")
plt.ylabel("Average Sleep Hours")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("average_sleep_line_plot.png", dpi=300)
plt.show()
