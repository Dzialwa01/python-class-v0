# Dzialwa Nemakonde
# 10 February 2026

# Task:
# Write a function `funny_phrase` that accepts a sentence string.
# The function should return the sentence where every other word has its vowels repeated twice consecutively.

import double_vowel # to access the double_vowel function

def funny_phrase(sentence):

    list1 = sentence.split(" ")

    for i in range(1, len(list1), 2):
        list1[i] =double_vowel.double_vowel(list1[i]) # utilizing the double_vowel function 

    return " ".join(list1) # to return the output as a string

print(funny_phrase("she dreamed of being a runner"))
# 'she dreeaameed of beeiing a ruunneer'

print(funny_phrase("park near the stoplight"))
# 'park neeaar the stoopliight'

print(funny_phrase("we need many gardeners"))
# 'we neeeed many gaardeeneers'