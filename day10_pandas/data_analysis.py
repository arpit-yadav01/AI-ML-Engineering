import pandas as pd

print("student analysis")

# Load CSV
df = pd.read_csv("students.csv")


print("\nFull Data:")
print(df)

print("\nBasic Info:")
print(df.info())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())


print("\nStudents Above 85 Marks:")
high_scorers = df[df["Marks"] > 85]
print(high_scorers)
