# Dzialwa Nemakonde
# 22 January 2026

# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.

def bleep_vowels(word):
    
    word1 = ""
    vowels = "aeiou"

    for ch in word:
        if ch in vowels: # checks if character is a vowel and adds a * instead
            word1 += "*"
        else:
            word1 += ch    # if char is not a vowel, the letter is added
    print(word1)        

# Example:
bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'

