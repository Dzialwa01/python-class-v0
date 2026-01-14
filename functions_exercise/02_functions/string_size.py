# Write a function `string_size` that accepts a string.
# Return:
#   "small"  → if length < 5
#   "medium" → if length == 5
#   "large"  → if length > 5

def string_size (string) :

    if len(string) < 5:
        return "small"
    elif len(string) == 5:
        return "medium"
    else:
        return "large"

print(string_size("cat"))          # "small"
print(string_size("bell"))         # "small"
print(string_size("ready"))        # "medium"
print(string_size("shirt"))        # "medium"
print(string_size("shallow"))      # "large"
print(string_size("intelligence")) # "large"

