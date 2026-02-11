# Dzialwa Nemakonde
# 11 February 2026

# Write a function `most_letter_word(sentence, char)` that accepts:
# - a sentence string
# - a single character
#
# The function should return the word in the sentence that contains the
# character the greatest number of times.
#
# You can assume the sentence contains at least one word.
# If there is a tie, return the word that appears first in the sentence.

def most_letter_word(sentence, char):

    words = sentence.split(" ")
    dict1 = {}
    count = 0

    for word in words:
        count = 0
        for ch in word:
            if ch == char: 
                count += 1 
        dict1[word] = count # to store the words and the number of letters in the word == char

    ans = [key for key in dict1.keys() if dict1[key] == max(dict1.values())] # making a list of all the words with the highest number of the character appearances

    return ans[0] # returning the word that appears first in the sentence.
                


print(most_letter_word(
'she received an award for excellence in science','e'
))# 'excellence'

print(most_letter_word(
'she received an award for excellence in science','a'
))# 'award'

print(most_letter_word(
'I hope sophomore year comes soon','o'
))# 'sophomore'

print(most_letter_word(
'I hope sophomore year comes soon','s'
))# 'sophomore'