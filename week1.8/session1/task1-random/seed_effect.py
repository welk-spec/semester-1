# See README.md for instructions on what to do this program

import random

random.seed(50)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

# the random.seed() sets the seed for the rng, and if it is set, 
# the numbers will be the same every time it is ran.
# when turned into a comment, the set number for a seed
# will disappear and the seed will be randomized