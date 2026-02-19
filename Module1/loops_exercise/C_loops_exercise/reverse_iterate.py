# Dzialwa Nemakonde
# 21 january 2026

# Write a function `reverse_iterate(text)` that prints each character of the string
# in reverse order. The function does not return a value, just prints.

def reverse_iterate (text):

    for i in range( len(text)-1, -1,-1): # ensuring it steps down from last index
        print(text[i])
        

# Example:
reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

reverse_iterate("box")
# x
# o
# b

