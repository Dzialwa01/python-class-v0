# Dzialwa Nemakonde
# 20 January 2026

# Write a function `product_up_to(max_num)` that returns the product of all numbers
# from 1 to max_num inclusive. (1*2*3*...*max_num)

def product_up_to(num):

    product = 1

    for i in range(1, num+1):
        product *= i

    print(product)    

# Example:
product_up_to(4) #-> 24
product_up_to(5) #-> 120
product_up_to(7) #-> 5040

