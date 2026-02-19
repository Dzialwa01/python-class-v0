# Dzialwa Nemakonde
# 10 February 2026

# Task:
# Write a function `pick_primes` that accepts a list of numbers.
# The function should return a new list containing only the prime numbers from the original list.

import is_prime

def pick_primes(list1):

    list2 = []

    for num in list1:
        if is_prime.is_prime(num) == True:
            list2.append(num)

    return list2        



print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []