# Dzialwa Nemakonde
# 22 January 2026

# Write a function `filter_long_words(words)` that accepts a list of strings.
# The function should return a new list containing only the words that have
# less than 5 characters.

def filter_long_words(words):

    list1 = [] # New list that the required words will be added in
    for i in range (len(words)):
        if len(words[i]) < 5: # ensures that only words ending with length less than 5 are added to the new list
            list1.append(words[i])

    print(list1)        

# Example:
filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]) #-> ['kale', 'cat', 'axe']
filter_long_words(["disrupt", "pour", "trade", "pic"]) #-> ['pour', 'pic']