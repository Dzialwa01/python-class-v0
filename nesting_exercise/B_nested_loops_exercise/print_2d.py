# Dzialwa Nemakonde
# 29 January 2026

# Write a function `print2d(matrix)` that accepts a 2D list and prints all inner elements.

def print2d(matrix):
    
    for list in matrix: # Takes one element in a the matrix which is list
        for j in range(len(list)): # to ensure that we iterate through the each list
            print(list[j])

array1 = [
    ["a", "b", "c", "d"],
    ["e", "f"],
    ["g", "h", "i"]
]

print2d(array1)
# prints:
# a
# b
# c
# d
# e
# f
# g
# h
# i

array2 = [[9, 3, 4], [11], [42, 100]]
print2d(array2)
# prints:
# 9
# 3
# 4
# 11
# 42
# 100

