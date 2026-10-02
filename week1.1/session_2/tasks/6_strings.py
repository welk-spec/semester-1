# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

# this prints the original string when user enters 
print(f"\nOriginal String: {user_string}")

# prints user input string, all in lowercase
print(f"Modified String 1: {user_string.lower()}")

# prints user input string, all in uppercase
print(f"Modified String 2: {user_string.upper()}")

# this removes dead only space at the start and end of a string
print(f"Modified String 3: {user_string.strip()}")

# this replaces characters in a string with another, this case its replacing 'a' with '@'
print(f"Modified String 4: {user_string.replace('a', '@')}")

# this capitalizes first letter of a string
print(f"Modified String 5: {user_string.capitalize()}")

# this reverses the string
print(f"Modified String 6: {user_string[::-1]}")

# this capitalizes the first letter of each word in a string
print(f"Modified String 7: {user_string.title()}")

# this prints out how much characters are in a string
print(f"Modified String 8: {len(user_string)}")

# prints out how many specified characters are in a string, in this case 'a'
print(f"Modified String 9: {user_string.find('a')}")

# counts how many times a character appears in a string, in this case 'a'
print(f"Modified String 10: {user_string.count('a')}")

# this checks if the string starts with hello, returning either true or false
print(f"Modified String 11: {user_string.startswith('Hello')}")

# this checks if the string ends with !. returning either true or false
print(f"Modified String 12: {user_string.endswith('!')}")

# this checks if the string is alphanumeric, returning either true or false
print(f"Modified String 13: {user_string.isalnum()}")

# this checks if the string is only letters, returning either true or false
print(f"Modified String 14: {user_string.isalpha()}")

# this checks if the string is only numbers, returning either true or false
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!