# Write a function `is_long` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# is longer than 5 characters.

def is_long (word):
    return len(word) > 5

print(is_long("pie"))         # False
print(is_long("kite"))        # False
print(is_long("kitty"))       # False
print(is_long("telescope"))   # True
print(is_long("thermometer")) # True
print(is_long("restaurant"))  # True

