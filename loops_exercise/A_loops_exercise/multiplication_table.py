# Dzialwa Nemakonde
# 20 January 2026

# Print the multiplication table of a number up to 10.

def multiplication_table(num):

    for i in range(1, 11): # range is 11 to ensure table is up to 10
        print(num * i)


multiplication_table(4)
# 4
# 8
# 12
# ...
# 40