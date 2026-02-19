# Write a function `larger(a, b)`

# Return the **larger** of the two numbers.

def larger(a, b):

    if a >= b:
        return a
    else:
        return b 

# **Example Output:**
print(larger(256, 400))   # 400
print(larger(31, 4))      # 31
print(larger(-6, 7))      # 7
print(larger(11.3, 11.2)) # 11.3
print(larger(-10, -3))    # -3

