# Dzialwa Nemakonde
# 04 February 2026

# Task:
# Write a function `letter_map` that accepts:
# - a string
# - a dictionary
# The function should return a new string where characters that appear as keys in the dictionary are replaced with their corresponding values.

def letter_map(string, dict1):

    new_string = ""

    for ch in string:
        if ch in dict1: 
            new_string += dict1[ch] # to return they value if the character is a key in the dictionary
        else:
            new_string += ch

    return new_string            

print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'