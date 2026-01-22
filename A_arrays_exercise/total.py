# Dzialwa Nemakonde
# 22 January 2026


# Write a function `total(numbers)` that accepts a list of numbers as an argument.
# The function should return the sum of all elements in the list.

def total(numbers):
    
    sum1 = 0

    for i in numbers:
        sum1 += i

    print(sum1)    

# Example:
total([3, 2, 8]) #-> 13
total([-5, 7, 4, 6]) #-> 12
total([7]) #-> 7
total([]) #-> 0

