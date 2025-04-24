import pandas as pd
import re
import matplotlib.pyplot as plt

# 1. Kalp atış verisini saat bazında çıkaran fonksiyon
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
                if 8 <= hour < 20:  # sadece 08:00–20:00 arası
                    bpm = float(value_match.group(1))
                    records.append((hour, bpm))
    return pd.DataFrame(records, columns=["hour", "bpm"])

# 2. Veriyi yükle ve ortalamaları hesapla
df = extract_heart_rate_by_hour("HKQuantityTypeIdentifierHeartRate.txt")  # ← dosya adını gerektiği gibi değiştir
hourly_avg = df.groupby("hour")["bpm"].mean()

# 3. Çizgi grafiği oluştur
plt.figure(figsize=(10, 5))
plt.plot(hourly_avg.index, hourly_avg.values, marker="o", color="crimson", linewidth=2)
plt.title("Average Heart Rate by Hour (08:00–20:00)")
plt.xlabel("Hour of the Day")
plt.ylabel("Average Heart Rate (BPM)")
plt.xticks(range(8, 21))
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("heart_rate_by_hour_line.png", dpi=300)
plt.show()
