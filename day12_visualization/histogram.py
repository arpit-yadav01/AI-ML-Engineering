import pandas as pd
import matplotlib.pyplot as plt

print("📊 Histogram - Marks Distribution")

# Load data
df = pd.read_csv("../day11_data_cleaning/messy_students.csv")

# Fill missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Histogram
plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()