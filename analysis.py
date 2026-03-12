import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sensor_data.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.describe())

df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Hour"] = df["Timestamp"].dt.hour

hourly_temp = df.groupby("Hour")["Temperature"].mean()

plt.figure()
plt.plot(hourly_temp)
plt.title("Average Temperature by Hour")
plt.xlabel("Hour")
plt.ylabel("Temperature")
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.title("Sensor Correlation")
plt.show()