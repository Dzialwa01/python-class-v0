# Dzialwa Nemakonde
# 19 January 2026
# Bonus 3

# Write a function that prints all indexes where a character appears in a string.

def find_char_positions(str1, char1):

    for i in range (len(str1)):
        if str1[i] == char1:
            print(i)

find_char_positions("banana", "a")
# 1
# 3
# 5

