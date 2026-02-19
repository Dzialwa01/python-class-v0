# Dzialwa Nemakonde
# 05 February 2026

# Task:
# Write a function `secret_cipher` that accepts:
# - a string
# - a dictionary (cipher map)
# Rules:
# - Replace each character in the string with its corresponding value from the dictionary
# - If a character does not exist as a key in the dictionary, replace it with`"?"`
# - Return the resulting string

def secret_cipher(string, dict1):

    for ch in string:
        if ch in dict1:
            string = string.replace(ch, dict1[ch])
        else:
            string = string.replace(ch, '?')

    return string            



print(secret_cipher("jello", {"j":"r","l":"s","e":"i" }))
# 'riss?'

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j" }))
# 'p?m?ojm'