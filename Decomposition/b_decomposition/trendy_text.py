# Dzialwa Nemakonde
# 11 February 2026

# Write a function `trendy_text` that accepts a sentence string as an argument.
# The function should return the sentence where the last vowel of every word
# is removed.

import remove_last_vowel # To access the remove_last_vowel function

def trendy_text(sentence):

    words = sentence.split(" ")
    words[-1] = remove_last_vowel.remove_last_vowel(words[-1])

    return " ".join(words)



print(trendy_text("the concert will be epic"))
# 'th concrt wll be epc'

print(trendy_text("breakfast food is wonderful"))
# 'breakfst fod s wonderfl'

print(trendy_text("the weather will improve hopefully"))
# 'th weathr wll improv hopeflly'

