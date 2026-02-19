# Dzialwa Nemakonde
# 19 january 2026

# Write a function `min_to_max(min_num, max_num)` that prints all numbers from min to max inclusive.

def min_to_max(min_num, max_num) :

    for i in range (min_num, max_num +1):
        print (i)



min_to_max(5, 9)
min_to_max(11, 13)

min_to_max(20, 11)   # what happens here? ^

# In the example above this will not output anything
# We can ensure that it does not matter if the max and min numbers are swapped by addition conditional statements as follows

# def min_to_max(min_num, max_num):

#     if max_num > min_num:
#         for i in range (min_num, max_num):
#             print(i)

#     else:       
#         for i in range (max_num, min_num):
#             print(i) 

