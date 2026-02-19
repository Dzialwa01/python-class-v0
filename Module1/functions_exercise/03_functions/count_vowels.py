# Extra no:2

# Write a function that returns how many vowels are in the string.

def count_vowels(word, count = 0):
    
    word1 = word.lower()
    vowels   = "aeiou"

    if len(word1) == 0:
        return count
    elif word1[0] in vowels:
        count += 1
        return count_vowels(word[1:], count)
    else:
        return count_vowels(word[1:], count)
    

print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3
print(count_vowels("Programming is a fun thing to do")) #9
