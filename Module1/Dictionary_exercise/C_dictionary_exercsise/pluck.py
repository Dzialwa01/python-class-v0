# Dzialwa Nemakonde
# 05 February 2026

# Task:
# Write a function `pluck` that accepts:
# - a dictionary
# - a list of strings
# The function should return a new dictionary containing only the key–value pairs where:
# - the key exists in the provided list

def pluck(dict1, lst):

    del_keys = []

    for key in dict1.keys():
        if key not in lst: 
            del_keys.append(key) # storing the keys to remove as python doesn't allow you to change a dictionary while looping over it

    for key in del_keys:
        dict1.pop(key) # removing the keys not in the list    

    return dict1 


print(pluck(
    {"name":"Fido","color":"Brown","breed":"German Shepherd" },
    ["name","breed"]
))
# { "name": "Fido", "breed": "German Shepherd" }

print(pluck(
    {"make":"Tesla","mpg":93,"model":"Model X","color":"white" },
    ["make","model"]
))
# { "make": "Tesla", "model": "Model X" }

