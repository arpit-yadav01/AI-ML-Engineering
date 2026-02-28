import pandas as pd

print("🧹 Data Cleaning Project")

df = pd.read_csv("messy_students.csv")

print("\nOriginal Data:")
print(df)

print("\nMissing Values Count:")
print(df.isnull().sum())

# Fill missing Marks with average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

# Create new feature
df["Pass"] = df["Marks"] >= 80

print("\nData with New Feature (Pass/Fail):")
print(df)