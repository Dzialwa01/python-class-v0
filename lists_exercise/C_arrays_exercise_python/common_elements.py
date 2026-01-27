# Dzialwa Nemakonde
# 27 January 2026

# Write a function `common_elements(arr1, arr2)` that accepts two lists as arguments.
# The function should return a new list containing the elements that are found in both input lists.
# The order of elements in the output list doesn't matter.

def common_elements(arr1, arr2):

    arr3 = []

    for char in arr1:
        if char in arr2: # checks if the character is in bot arrays
            arr3.append(char)

    print(arr3)        

# Example:
common_elements(["a", "c", "d", "b"], ["b", "a", "y"]) #-> ['a', 'b']
common_elements([4, 7], [32, 7, 1, 4]) #-> [4, 7]

