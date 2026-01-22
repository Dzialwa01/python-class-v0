# Dzialwa Nemakonde
# 22 January 2026

# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

def strings_to_lengths(strings):

    list1 = [] # The list that will store the numbers

    for i in range(len(strings)):
        length = len(strings[i])
        list1.append(length) # adds the length of the words to the new list

    print(list1)    


# Example:
strings_to_lengths(["belly", "echo", "irony", "pickled"]) #-> [5, 4, 5, 7]
strings_to_lengths(["on", "off", "handmade"]) #-> [2, 3, 8]