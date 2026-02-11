# Dzialwa Nemakonde
# 11 February 2026

# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

def remove_last_vowel(string):

    vowels = "aeiou"
    str1 = string

    for i in range(len(str1)-1,-1, -1):

        if str1[i] in vowels:
            first = str1[0:i]
            second = str1[i+1:] # to ensure the vowel is not included
            return first + second
        
    return str1    
    
    

print(remove_last_vowel("speaker"))# 'speakr'
print(remove_last_vowel("trading"))# 'tradng'
print(remove_last_vowel("thunder"))# 'thundr'
print(remove_last_vowel("myth"))# 'myth'

