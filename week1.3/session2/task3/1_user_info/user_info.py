# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

name = input("name: ")
age = input("age: ")
favorite_colour = input("favorite colour: ")

# Open a file called 'user_info.txt' for writing

with open('user_info.txt', 'w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Favorite Colour: {favorite_colour}\n")

# Write each piece of information to the file, each on a new line.

with open('user_info.txt', 'r') as file:
    content = file.read()
    print(content)

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'