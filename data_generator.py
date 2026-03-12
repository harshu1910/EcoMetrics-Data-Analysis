import pandas as pd
import numpy as np
from datetime import datetime

# date range from 2010 to 2026
timestamps = pd.date_range(
    start="2010-01-01",
    end="2026-12-31",
    freq="1H"   # 1 hour interval
)

rows = len(timestamps)

# simulate realistic sensor behaviour
temperature = 22 + 5*np.sin(np.arange(rows)/24*2*np.pi) + np.random.normal(0,1,rows)
humidity = 60 - 0.4*temperature + np.random.normal(0,2,rows)
air_quality = np.random.normal(100,20,rows)
co2 = np.random.normal(420,25,rows)

df = pd.DataFrame({
    "Timestamp": timestamps,
    "Temperature": temperature,
    "Humidity": humidity,
    "AirQuality": air_quality,
    "CO2": co2
})

df = df.round(2)

# save dataset
df.to_csv("sensor_data_2010_2026.csv", index=False)

print("Dataset Generated Successfully")
print("Total Rows:", len(df))