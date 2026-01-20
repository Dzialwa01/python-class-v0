# Dzialwa Nemakonde
# 20 January 2026

# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

def sum_up_to(max_num):
    
    add = 0 # it get updated with each loop

    for i in range(1, max_num + 1):
        add += i

    print(add)

# Example:
sum_up_to(4)  #-> 10
sum_up_to(5)  #-> 15
sum_up_to(2)  #-> 3

