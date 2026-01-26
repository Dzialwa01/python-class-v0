# Dzialwa Nemakonde
# 26 January 2026

# Write a function `your_average_function(numbers)` that accepts a list of numbers.
# The function should return the average of all elements in the list.
# If the list is empty, the function should return None.

def your_average_function(numbers):

    sum1 = 0
    for num in numbers:
        sum1 += num

    if len(numbers) == 0: # Checking if list is empty
        print("None")
    else:
        print(sum1 / len(numbers))


     


# Example:
your_average_function([5, 2, 7, 24]) # 9.5
your_average_function([100, 6]) # 53
your_average_function([31, 32, 40, 12, 33]) # 29.6
your_average_function([]) # None

