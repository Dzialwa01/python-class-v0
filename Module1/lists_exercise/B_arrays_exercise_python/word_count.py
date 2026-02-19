# Dzialwa Nemakonde
# 26 January 2026

# Write a function `word_count(sentence, target_words)` that accepts a sentence string and a list of target words.
# The function should return a count of how many words in the sentence are also in target_words.

def word_count(sentence, target_words):

    count = 0
    for word in sentence.split(" "): # splitting the sentence into a list of words
        if word in target_words:
            count += 1 

    print(count)        

# Example:
word_count("open the window please", ["please", "open", "sorry"]) # 2
word_count("drive to the cinema", ["the", "driver"]) # 1
word_count("can I have that can", ["can", "I"]) # 3

