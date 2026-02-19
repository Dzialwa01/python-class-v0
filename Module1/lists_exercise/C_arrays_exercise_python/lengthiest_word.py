# Dzialwa Nemakonde
# 27 January 2026

# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

def lengthiest_word(sentence):

    words = sentence.split(" ")
    answer = ""

    for word in words:
        if len(word) >= len(answer): # to compare the lengths of the words and ensure that the longer one is assigned to answer
            answer = word

    print(answer)        


#Example:
lengthiest_word("I am pretty hungry") #-> 'hungry'
lengthiest_word("we should think outside of the box") #-> 'outside'
lengthiest_word("down the rabbit hole") #-> 'rabbit'
lengthiest_word("simmer down") #-> 'simmer'

