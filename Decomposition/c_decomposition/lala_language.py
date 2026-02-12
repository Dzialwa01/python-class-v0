# Dzialwa Nemakonde
# 12 February 2026

# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

def lala_language(sentence):

    words = sentence.split(" ")
    lst = []
    vowels = "aeiou"

    for word in words:

        if len(word) > 3:
            for ch in word:
                if ch in vowels: 
                    word = word.replace(ch, ch + "l" + ch) # to add the "l" and the same letter in the sentence.
            lst.append(word)   
        else: # just adds the word in the list if it has less than 3 letters
            lst.append(word)        

    return " ".join(lst)         


print(lala_language('this is pretty strange'))
# 'thilis is preletty stralangele'

print(lala_language('can you speak our language'))
# 'can you spelealak our lalangulualagele'
