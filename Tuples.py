# Tuples

Fruits = ("Orange", "Apple", "Banana", "Guava")
print(type(Fruits))
print(Fruits)

Mix = ("Gaurav", 19, True, "Male")
print(Mix)

print(Mix[2])

# Add items

Mix_List = list(Mix)

Mix_List.append("Sharma")

Mix = tuple(Mix_List)
print(Mix)

# deleting tuple

del Fruits
