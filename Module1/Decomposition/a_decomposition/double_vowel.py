# Dzialwa Nemakonde
# 10 February 2026

# Task:
# Write a function `double_vowel` that accepts a string as an argument.
# The function should return a new string where every vowel in the original string is repeated twice consecutively.

def double_vowel(string):

    str1 = ""
    vowels = "aeiou"

    for ch in string:
        if ch in vowels:
           str1 += ch*2 # double the character if it is a vowel
        else:
            str1 += ch   

    return str1


print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'


