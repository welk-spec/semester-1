# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database

rivers["York"] = "Ouse"

# Display all the keys

test = rivers.keys()
x = print(test)

# Display all the values


get = rivers.get(x)
print(get)

# Display all the key:value pairs, as tuples

item = rivers.items()
print(item)

# Delete an entry from the rivers database

y = rivers.pop("London")
print(rivers)