# Dzialwa Nemakonde
# 02 Febryary 2026

# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.

def shorten_long_words(sentence):
    
    vowels = "aeiou"
    sentence1 = sentence.split() 
    new_sentence = []

    for word in sentence1:
        if len(word) <= 4:
            new_sentence.append(word) # to ensure words with 4 characters or less are added as they are 
        else:
            for i in word:
                if i in vowels:
                    word = word.replace(i, "") # removes the vowel by replacing them with and empty string
            new_sentence.append(word)        
                        
    return " ".join(new_sentence) # to return the output as a string and not a list
            
            
# Example usage:
print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'