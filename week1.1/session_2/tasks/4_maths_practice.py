# Work out the answers to the three maths problems:

# 1: (4 x 8) x 6

number1 = 4
number2 = 8
number3 = 6
result1 = (number1 * number2) * number3

# 2: (2^3) / (8/3)

number4 = 2
number5 = 3
number6 = 8
number7 = 3
result2 = (number4 ** number5) / (number6 / number7)

# 3: 27^2 x 19/4

number8 = 27
number9 = 2
number10 = 19
number11 = 4
result3 = (number8 ** number9) * (number10 / number11)

input("which one do you wanna see: ")
if input := "1":
    print(f"the answer is : {result1}")

if input := "2":
    print(f"the answer is : {result2}")
    
if input := "3":
    print(f"the answer is : {result3}")
