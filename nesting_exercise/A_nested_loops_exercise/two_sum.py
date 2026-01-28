# Dzialwa Nemakonde
# 28 January 2026

# Write a function `two_sum(numbers, target)` that accepts a list of numbers and a target number.
# The function should return True if there exists a pair of distinct elements in the list that sum to the target.
# Otherwise, return False.

def two_sum(numbers, target):

    bool1 = False
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)): # i+1 ensures that distinct elements are taken
            if numbers[i] + numbers[j] == target:
                bool1 = True 
                break # to  stop the loop if there are two numbers equal to target. 
    print(bool1)

# Example:
two_sum([2, 3, 5, 9], 7) #-> True
two_sum([2, 3, 5, 9], 4) #-> False
two_sum([6, 3, 4], 10) #-> True
two_sum([6, 5, 1], 10) #-> False

