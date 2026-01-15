# Extra no:3

# Write a function that checks if a string is a **palindrome** (same forward & backward).

# Ignore spaces and capitalization.

def is_palindrome(string):

    string1 = string.lower().replace(" ","")
    return string1 == string1[::-1]

print(is_palindrome("level"))          # True
print(is_palindrome("Race car"))       # True
print(is_palindrome("python"))         # False

