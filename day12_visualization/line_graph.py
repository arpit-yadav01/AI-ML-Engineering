import pandas as pd
import matplotlib.pyplot as plt

print("📈 Line Graph - Marks Trend")

# Load data
df = pd.read_csv("../day11_data_cleaning/messy_students.csv")

# Fill missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Line Graph
plt.figure()
plt.plot(df["Marks"])
plt.title("Marks Trend")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.show()