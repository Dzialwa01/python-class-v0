# Dzialwa Nemakonde
# 10 February 

# Task:
# Write a function `is_prime` that accepts a number as an argument.
# The function should return `True` if the number is prime, otherwise return `False`.

# A prime number:

# - Is greater than 1
# - Is divisible only by 1 and itself

def is_prime(num):

    if num < 2:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False # returns false if the number is divisible by other numbers between 1 and itself
        
    return True    


print(is_prime(11))# True
print(is_prime(8))# False
print(is_prime(7))# True
print(is_prime(21))# False
print(is_prime(2))# True
print(is_prime(15))# False
print(is_prime(1))# False