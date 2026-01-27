# Dzialwa Nemakonde
# 27 January 2026

# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

def alternating_caps(sentence):

    list1 = sentence.split(" ")
    list2 = []

    for i in range(len(list1)):
        if i % 2 != 0: # to make words in odd indices uppercase and add them to list
            list2.append(list1[i].upper()) 
        else:
            list2.append(list1[i].lower())

    print(" ".join(list2)) # to combine the words in a list into a sentence           
    

# Example:
alternating_caps("take them to school") #-> 'take THEM to SCHOOL'
alternating_caps("What did ThEy EAT before?") #-> 'what DID they EAT before?'

