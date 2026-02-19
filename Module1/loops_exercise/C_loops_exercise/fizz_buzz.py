# Dzialwa Nemakonde
# 26 January 2026

# Write a function `fizz_buzz(max_num)` that prints all numbers <= max_num
# that are divisible by 3 or 5 but not both.
# The function does not return a value, just prints.

def fizz_buzz(max_num):

    for i in range (1, max_num + 1):

        if (i % 3 == 0) or (i % 5 == 0):

            if not ((i % 3 == 0) and (i % 5 == 0)): # ensures that numbers that both 3 and 5 divide are ignored
                print(i)

# Example:
fizz_buzz(18)
# 3
# 5
# 6
# 9
# 10
# 12
# 18

fizz_buzz(33)
# 3
# 5
# 6
# 9
# 10
# 12
# 18
# 20
# 21
# 24
# 25
# 27
# 33