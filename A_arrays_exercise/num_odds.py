# Dzialwa Nemakonde
# 22 January 2026

# Write a function `num_odds(numbers)` that accepts a list of numbers.
# The function should return the count of odd numbers in the list.

def num_odds(numbers):

    count = 0

    for i in numbers:
        if i % 2 != 0: #to check if numbers are truly odd
            count += 1

    print(count)      
    

# Example:
num_odds([4, 7, 2, 5, 9]) #-> 3
num_odds([11, 31, 58, 99, 21, 60]) #-> 4
num_odds([100, 40, 4]) #-> 0