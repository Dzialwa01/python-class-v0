# Dzialwa Nemakonde
# 04 February 2026

# Task:
# Write a function `most_common_letter` that accepts a string as an argument.
# The function should return the character that appears most frequently in the string.
# You may assume:
# - There are no ties
# - The string contains only lowercase letters

def most_common_letter(string):

    dict1 = {}

    for ch in string: # to keep count of the number of times a character appears in the string
        if ch in dict1: 
            dict1[ch] += 1 
        else:
            dict1[ch] = 1

    ans = [k for k in dict1.keys() if dict1[k] == max(dict1.values())] # Obtaining the key with the highest value        

    return ans[0] # ensuring the output is a string

print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'

