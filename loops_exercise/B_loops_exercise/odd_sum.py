# Dzialwa Nemakonde
# 20 January 2026

# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

def odd_sum(num):

    sum1 = 0

    for i in range(1, num + 1):

        if i % 2 != 0: # To ensure that the numbers added to sum1 are odd numbers
            sum1 += i

    print(sum1)        

# Example:
odd_sum(10) #-> 25  # 1 + 3 + 5 + 7 + 9
odd_sum(5)  #-> 9   # 1 + 3 + 5

