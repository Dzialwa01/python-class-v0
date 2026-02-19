# Dzialwa Nemakonde
# 27 January 2026

# Write a function `remove_short_words(sentence)` that accepts a string containing a sentence.
# The function should return a new sentence where all words shorter than 4 characters are removed.

def remove_short_words(sentence):

    new_sentence = ""
    list1 = sentence.split(" ")

    for word in list1:
        if len(word) >= 4: # to ensure that only words with length > 4 are added to list
            new_sentence += word + " "

    print(new_sentence)        

# Example:
remove_short_words("knock on the door will you") #-> 'knock door will'
remove_short_words("a terrible plan") #-> 'terrible plan'
remove_short_words("run faster that way") #-> 'faster that'

