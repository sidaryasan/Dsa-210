import pandas as pd
import re
import matplotlib.pyplot as plt

# 1. Function to extract hourly heart rate values from Apple Health export
def extract_heart_rate_by_hour(filepath):
    records = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if 'HKQuantityTypeIdentifierHeartRate' not in line:
                continue
            time_match = re.search(r'startDate="(.*?)"', line)
            value_match = re.search(r'value="([\d.]+)"', line)
            if time_match and value_match:
                timestamp = pd.to_datetime(time_match.group(1))
                hour = timestamp.hour
                if 8 <= hour < 20:  # filter only 08:00–20:00
                    bpm = float(value_match.group(1))  # beats per minute
                    records.append((hour, bpm))
    return pd.DataFrame(records, columns=["hour", "bpm"])

# 2. Load the data and calculate average BPM per hour
df = extract_heart_rate_by_hour("HKQuantityTypeIdentifierHeartRate.txt")  # adjust file path if needed
hourly_avg = df.groupby("hour")["bpm"].mean()

# 3. Plot the line graph
plt.figure(figsize=(10, 5))
plt.plot(hourly_avg.index, hourly_avg.values, marker="o", color="crimson", linewidth=2)
plt.title("Average Heart Rate by Hour (08:00–20:00)")
plt.xlabel("Hour of the Day")
plt.ylabel("Average Heart Rate (BPM)")
plt.xticks(range(8, 21))  # ticks for 08:00 to 20:00
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("heart_rate_by_hour_line.png", dpi=300)  # save to file
plt.show()
