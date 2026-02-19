# Dzialwa Nemakonde
# 02 February 2026

# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.

def remove_first_vowel(s):

    letters = list(s)
    vowels = "aeiou"

    for char in letters:
        if char in vowels: # to check if the character is a vowel so it can be removed
            letters.remove(char) 
            break # ensures that the loop breaks once the first vowel is removed

    return ''.join(letters) # returning the output as a string

# Example usage:
print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'