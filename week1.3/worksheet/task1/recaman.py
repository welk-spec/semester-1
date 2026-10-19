# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence

sequence = [0]
for i in range(1, L):
    n = sequence[-1] - i
    if n > 0 and n not in sequence:
        sequence.append(n)
    else:
        n = sequence[-1] + i
        sequence.append(n)


# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence