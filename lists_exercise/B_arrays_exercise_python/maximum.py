# Dzialwa Nemakonde
# 26 January 2026

# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(numbers):

    if len(numbers) == 0: # Checking if list is empty
        print("None")

    else:
        ans = 0
        for num in numbers:
            if num > ans: 
                ans = num # ensures that ans is assigned to the bigger number in each iteration

        print(ans)        



# Example:
maximum([5, 6, 3, 7]) # 7
maximum([17, 15, 19, 11, 2]) # 19
maximum([]) # None

