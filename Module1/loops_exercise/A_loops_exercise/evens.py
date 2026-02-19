# Dzialwa Nemakonde
# 19 january 2026

# Write a function `evens(max_num)` that prints all positive even numbers LESS than max_num.

def evens(max_num):

    for i in range(1, max_num):
        if i % 2 == 0 : # Checks if the number is even
            print (i)
            

evens(11)
evens(8)

