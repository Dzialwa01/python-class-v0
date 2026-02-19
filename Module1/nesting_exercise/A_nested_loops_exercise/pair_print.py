# Dzialwa Nemakonde
# 28 January 2026

# Write a function `pair_print(arr)` that accepts a list and prints all unique pairs
# of elements in the list. It doesn't need to return anything.

def pair_print(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            print(f" {arr[i]} - {arr[j]}")

# Example:
pair_print(["artichoke", "broccoli", "carrot", "daikon"])

# prints
# artichoke - broccoli
# artichoke - carrot
# artichoke - daikon
# broccoli - carrot
# broccoli - daikon
# carrot - daikon

