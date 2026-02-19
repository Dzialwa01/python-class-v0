# Dzialwa Nemakonde
# 20 January 2026

# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

def string_repeater(text, n):

    word = ""

    for i in range (1, n+1): # problem can be solved using just print(text * n)
        word += text

    print(word)    

# Example:
string_repeater("go", 2) #-> 'gogo'
string_repeater("tac", 3) #-> 'tactactac'

