# Dzialwa Nemakonde
# 12 February 2026

# Write a function `censor_sentence(sentence, target_words)` that accepts:
# - a sentence string
# - a list of target words
#
# The function should return a new sentence where each target word
# is replaced with '*' characters of the same length.

def censor_sentence(sentence, target_words):

    words = sentence.split(" ")

    for i in range(len(words)):

        w = words[i]
        if w in target_words:
            words[i] = "*" * len(w) # ensuring that the * matches the characters in the word

    return " ".join(words)        

print(censor_sentence('where the heck is my celery', ['heck','celery']))
# 'where the **** is my ******'

print(censor_sentence('why you little sweetheart', ['sweetheart','salad']))
# 'why you little **********'
