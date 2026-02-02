# Dzialwa Nemakonde
# 02 February 2026

# Write a function `spam(pairs)` that accepts a 2D list. Each inner list contains
# a word and a number. The function returns a string with each word repeated
# the specified number of times, separated by spaces.

def spam(pairs):

    sentence = ""
    for lst in pairs:
        sentence += (lst[0] + ' ')*lst[1] 
    
    return sentence
        

# Example usage:
array1 = [["hi", 3], ["bye", 2]]
print(spam(array1))  # 'hi hi hi bye bye'

array2 = [["cat", 1], ["dog", 2], ["bird", 4]]
print(spam(array2))  # 'cat dog dog bird bird bird bird'