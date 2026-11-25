import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
# pandas.DataFrame, from using print(type(data))

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.

print(data)

# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students

total_students = len(data)
print(f"Total number of students: {total_students}")

# Find the mean average GPA of the students

mean_gpa = data['GPA'].mean()
print(f"Mean average GPA: {mean_gpa}")

# Find the standard deviation of how much sleep students get per day

std_sleep = data['Sleep_Hours_Per_Day'].std()
print(f"Standard deviation of sleep hours: {std_sleep}")

# Find the maximum amount of study hours per day

max_study_hours = data['Study_Hours_Per_Day'].max()
print(f"Maximum study hours per day: {max_study_hours}")

# Sort the students by social hours per day ascending (lowest -> highest)

data_sorted = data.sort_values(by='Social_Hours_Per_Day', ascending=True)
print(data_sorted)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

data['Total_hours'] = data['Study_Hours_Per_Day'] + data['Sleep_Hours_Per_Day'] + data['Social_Hours_Per_Day']

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.

high_low_stress_students = data[data['Stress_Level'].isin(['High', 'Low'])]
print(f"Students with high or low stress level:")
print(high_low_stress_students)

# Can you work out whether having a higher stress level leads to a higher GPA?

high_stress_gpa = data[data['Stress_Level'] == 'High']['GPA'].mean()
low_stress_gpa = data[data['Stress_Level'] == 'Low']['GPA'].mean()
print(f"Average GPA of high stress students: {high_stress_gpa}")
print(f"Average GPA of low stress students: {low_stress_gpa}")