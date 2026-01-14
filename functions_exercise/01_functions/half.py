# Write a function `half` that accepts a number as an argument.
# The function should return half of the number.

def half(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num / 2
    
print(half(8))    # 4
print(half(15))   # 7.5
print(half(90))   # 45