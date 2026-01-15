# Write average_of_four(a, b, c, d) that returns the average of four numbers.


def average_of_four(a, b, c, d):

    sum1 = a+ b + c + d
    if (sum1) % 2 == 0:
        return sum1 // 4
    else:
        return sum1 / 4
# Example Output:

print(average_of_four(10, 4, 12, 3))     # 7.25
print(average_of_four(-20, 50, 4, 21))   # 13.75
print(average_of_four(5, 5, 3, 7))       # 5

