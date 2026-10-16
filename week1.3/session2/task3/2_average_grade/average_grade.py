# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

with open('student_data.csv', 'r') as file:
    data = file.readlines()[1:]

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3

averages = []
for line in data:
    student_info = line.strip().split(',')
    name = student_info[1]
    grades = list(map(int, student_info[2:]))
    average_grade = sum(grades) / len(grades)
    averages.append((name, average_grade))
    print(f"{name}'s average grade: {average_grade:.2f}")

# Open a file called 'report.txt'

with open('report.txt', 'w') as report_file:
    for name, average in averages:
        report_file.write(f"{name}: {average:.2f}\n")


# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
