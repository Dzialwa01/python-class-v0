# Dzialwa Nemakonde
# 22 January 2026


# Write a function `stay_positive(numbers)` that accepts a list of numbers.
# The function should return a new list containing only the positive numbers.

def stay_positive(numbers):

    list1 = []

    for i in numbers:
        if i > 0: # checks if number is positive then adds onto the list
            list1.append(i)

    print(list1)        



# Example:
stay_positive([10, -4, 3, 6]) #-> [10, 3, 6]
stay_positive([-5, 11, -40, 30.3, -2]) #-> [11, 30.3]
stay_positive([-11, -30]) #-> []

