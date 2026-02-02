# Dzialwa Nemakonde
# 02 February 2026

# Write a function `remove_vowels(s)` that accepts a string and returns a new string
# with all vowels removed (a, e, i, o, u).

def remove_vowels(s):

    vowels = "aeiou"
    letters = list(s) # to iterate easily and also using list methods

    for char in letters:
        if char in vowels:
            letters.remove(char) # to remove the characters found as vowels

    return ''.join(letters) # return the output as a string again

# Example usage:
print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'