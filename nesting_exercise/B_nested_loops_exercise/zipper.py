# Dzialwa Nemakonde
# 29 January 2026

# Write a function `zipper(list1, list2)` that returns a 2D list containing pairs of elements at
# the same indices. Assume lists have same length.

def zipper(list1, list2):

    final_list = []

    for i in range(len(list1)):
        final_list.append([list1[i], list2[i]]) # Adding pairs of elements at the same index on the two lists
    return final_list
        
array1 = ["a", "b", "c", "d"]
array2 = [-1, -2, -3, -4]
print(zipper(array1, array2))

array3 = ["whisper", "talk", "shout"]
array4 = ["quiet", "normal", "loud"]
print(zipper(array3, array4))