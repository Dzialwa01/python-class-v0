# Dzialwa Nemakonde
# 19 January 2026
# Bonus no1

# Write `sum_of_range(n)`
# Print the sum of numbers from 1 to n.

def sum_of_range(num):

    sum1 = 0
    for i in range(1, num+1):
        sum1 += i # adds the numbers from 1 to num consecutively in each iteration

    print(sum1)    


sum_of_range(5)
# prints: 15

