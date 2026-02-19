# Extra no:4
# Write `sum_upto(n)`
# Return the sum of numbers from 1 → n.

def sum_upto(num, sum1 = 0):

    if num == 0:
        return sum1
    else:
        sum1 += num
        return sum_upto(num-1, sum1)
    

print(sum_upto(5))   # 15
print(sum_upto(10))  # 55
