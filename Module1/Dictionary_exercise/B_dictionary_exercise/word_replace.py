# Dzialwa Nemakonde
# 04 February 2026

# Task:
# Write a function `word_replace` that accepts:
# - a sentence string
# - a dictionary
# The function should return a new sentence where words that appear as keys in the dictionary are replaced with their corresponding values.

def word_replace(string, dict1):

    words = string.split(" ") # to obtain a list of the words
    
    for word in words:
        if word in dict1: # to check if the word is a key in dict and replacing it with its value if it is.
           string = string.replace(word, dict1[word])

    return string        

print(word_replace(
"I never take naps during the day",
    {"never":"always","day":"weekend" }
))
# 'I always take naps during the weekend'

print(word_replace(
"the park is closed",
    {"closed":"open","the":"a" }
))
# 'a park is open'

print(word_replace(
"I do what I want",
    {"I":"we","cat":"dog" }
))
# 'we do what we want'