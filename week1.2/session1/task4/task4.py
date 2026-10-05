# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here? finds somethign that appears in both

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items? elements from both sets

food = fruit.union(vegetables)
print(food)

# Add an item to fruit

fruit.add("banana")
print(fruit)

# Remove an item from vegetables

vegetables.discard("potato")

# Find and display symmetric difference of the two sets

test = fruit.symmetric_difference(vegetables)
print(test)