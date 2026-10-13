# Worksheet 1.2: Task 1 Solution

import sys

try:
    grade = int(input("enter your grade from 0 to 100: "))
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade < 40 and grade >= 0:
    print(f"{grade} is a Fail.")
elif grade >= 40 and grade < 70:
    print(f"{grade} is a Pass.")
elif grade >= 70 and grade <= 100:
    print(f"{grade} is a Distinction.")
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")