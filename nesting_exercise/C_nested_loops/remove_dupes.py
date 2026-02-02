# Dzialwa Nemakonde
# 02 February 2026

# Write a function `remove_dupes(lst)` that accepts a list and returns a new list where each element appears only once.

def remove_dupes(lst):

    new_list = []

    for char in lst:
        if char not in new_list: # to ensure that we do not add duplicates
            new_list.append(char)
    return new_list         


# Example usage:
print(remove_dupes(["x", "y", "y", "x", "z"]))  # ['x', 'y', 'z']
print(remove_dupes([False, False, True, False]))  # [False, True]
print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7]))  # [42, 5, 7, 3]