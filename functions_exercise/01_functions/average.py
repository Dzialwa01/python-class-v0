# Write a function `average` that accepts three numbers as arguments.
# The function should return the average of the three numbers.

def average (num1, num2, num3):
    sum1 = num1 + num2 + num3
    return sum1 // 3

print(average(3, 10, 8))    # 7
print(average(10, 5, 12))   # 9
print(average(6, 20, 40))   # 22
