import random

# Get user to input how many random numbers they want

number = int(input("how many numbers do you want? "))

# Generate this many random numbers

random_number = [random.randint(1, 100) for i in range(number)] # Generate a list of random numbers between 1 and 100

# Write the random numbers to a file named random.txt, one number per line

with open("random.txt", "w") as outfile:
    for num in random_number:
        outfile.write(f"{num}\n")