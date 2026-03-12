import pandas as pd

df = pd.read_csv("sensor_data_2010_2026.csv")

df.to_excel("sensor_data_2010_2026.xlsx", index=False)

print("Excel file created successfully")