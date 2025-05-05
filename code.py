import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Excel file
df = pd.read_excel("Case_Study_5_B.xlsx", usecols=["Name", "Marks"])

df["Percentage"] = (df["Marks"] / 15) * 100

above_75 = df[df["Percentage"] > 75]
between_60_75 = df[(df["Percentage"] >= 60) & (df["Percentage"] <= 75)]
below_60 = df[df["Percentage"] < 60]

print("\nStudents with >75%:")
print(above_75[["Name", "Percentage"]])

print("\nStudents with 60–75%:")
print(between_60_75[["Name", "Percentage"]])

print("\nStudents with <60%:")
print(below_60[["Name", "Percentage"]])

plt.figure(figsize=(8, 5))
plt.hist(df["Percentage"], bins=np.arange(0, 105, 5), color='purple')
plt.xlabel("Percentage")
plt.ylabel("Number of Students")
plt.title("Histogram Plot")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(range(len(df)), df["Percentage"], color='green')
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.title("Scatter Plot")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
