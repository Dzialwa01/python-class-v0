# Dzialwa Nemakonde
# 04 February 2026

# Task:
# Write a function `get_average_age` that accepts a list of dictionaries.
# Each dictionary represents a person and contains an `age` key.
# The function should return the **average age** of all people.

def get_average_age(list1):

    sum1 = 0

    for dict1 in list1:
        sum1 += dict1["age"] # adds all the people's ages in the list

    avg = sum1 / (len(list1))

    return round(avg,2) # ensuring the answer is rounded to two decimals


peeps = [
    {"name":"Lovelace","age":36,"born":"London, UK" },
    {"name":"Kleene","age":85,"born":"Connecticut, US" },
    {"name":"Turing","age":41,"born":"London, UK" },
    {"name":"Hopper","age":85,"born":"New York, US" },
]

print(get_average_age(peeps))
# 61.75


people = [
    {"name":"Orwell","age":46,"born":"Bihar, India" },
    {"name":"Bradbury","age":91,"born":"California, US" },
    {"name":"Huxley","age":69,"born":"California, US" },
]

print(get_average_age(people))
# 68.67