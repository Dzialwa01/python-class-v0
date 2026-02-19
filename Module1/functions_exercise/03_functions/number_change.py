# Write a function:

# - If number is **even**, return **half**
# - If number is **odd**, return **double**


def number_change(num):
    
    if num % 2 == 0:
        return num // 2
    else:
        return num * 2
    
# **Example Output:**

print(number_change(6))   # 3
print(number_change(7))   # 14
print(number_change(16))  # 8
print(number_change(21))  # 42

