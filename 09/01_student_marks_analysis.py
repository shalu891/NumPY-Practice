import numpy as np

students = np.array(["Aman", "Riya", "Karan", "Priya", "Rahul"])
marks = np.array([78, 85, 92, 67, 88])

average = np.mean(marks)

print("STUDENT MARKS ANALYSIS")
print("-" * 30)

for name, mark in zip(students, marks):
    print(f"{name}: {mark}")

print("-" * 30)
print("Total Marks:", np.sum(marks))
print("Average Marks:", average)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

print("\nAbove Average:")
print(students[marks > average])

print("\nTop Scorer:")
print(students[marks == np.max(marks)])