# Dzialwa Nemakonde
# 26 January 2026

# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

def reverse_array(arr):

    list1 = []

    for i in range(len(arr) -1, -1, -1): # ensures the loop start from the last index going backwards 
        list1.append(arr[i]) # adds the elements to the new list in reverse order

    print(list1)    

# Example:
reverse_array(["zero", "one", "two", "three"]) # ['three', 'two', 'one', 'zero']
reverse_array([7, 1, 8]) # [8, 1, 7]

