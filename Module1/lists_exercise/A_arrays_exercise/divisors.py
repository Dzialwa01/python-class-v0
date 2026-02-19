# Dzialwa Nemakonde
# 22 January 2026

# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.

def divisors(num):

    divs = []
    for i in range(1, num + 1):
        if num % i == 0: # to check if the number divides num exactly, then it is added
            divs.append(i)

    print(divs)        

# Example:
divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]
