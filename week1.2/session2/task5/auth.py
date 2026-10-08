# Week 1.2, Session 2: Task 5
# Authentication

# Predefined credentials

correct_username = "1"
correct_password = "1"
two_factor_enabled = True
correct_2fa_code = "1"

# Ask user for their username and password

username = input("Enter your username: ")
password = input("Enter your password: ")

# Conditional block for login authentication
wrong_username = username != correct_username
wrong_password = password != correct_password
correct_2fa_code = two_factor_code

if not wrong_username and not wrong_password:
    if two_factor_enabled:
        two_factor_code = input("Enter the 2FA code sent to your device: ")
        if correct_2fa_code == two_factor_code:
            print("Login successful! Welcome!")
        else:
            print("Invalid two-factor authentication code. Access denied.")
    else:
        print("Login successful! Welcome!")
else:
    print("Invalid username or password. Access denied.")
