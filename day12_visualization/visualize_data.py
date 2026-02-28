import pandas as pd
import matplotlib.pyplot as plt

print("📊 Data Visualization Project")

# Load data
df = pd.read_csv("../day11_data_cleaning/messy_students.csv")

# Fill missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Bar Chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()