# Dzialwa Nemakonde
# 12 February 2026

# Write a function `pick_perfect_squares` that accepts a list of numbers.
# The function should return a list containing only the perfect squares.
#
# A perfect square is a number that can be written as n * n.

def pick_perfect_squares(lst):

    ans_list = []

    for num in lst:
        for i in range(num):

            if i*i > num: # adding this to eliminate the number of interations
                break
            elif i*i == num:
                ans_list.append(num)

    return ans_list            

print(pick_perfect_squares([6,4,81,21,36]))
# [4, 81, 36]

print(pick_perfect_squares([100,24,144]))
# [100, 144]

print(pick_perfect_squares([30,25]))
# [25]