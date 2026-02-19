# Dzialwa Nemakonde
# 05 February 2026

# Task:
# Write a function `object_add` that accepts two dictionaries containing numeric values.
# Rules:
# - If a key appears in both dictionaries, sum their values
# - If a key appears in only one dictionary, keep its value as-is
# - Return a new dictionary

def object_add(dict1, dict2):

    ans_dict = {}
    both_dicts = dict1 | dict2 # merging the dictionaries to access the key's value if its not in both dictionaries

    for key in both_dicts.keys(): 
        if key in dict1.keys(): 
            if key in dict2.keys(): # checks if key is in both dictionaries
                ans_dict[key] = dict1[key] + dict2[key]
            else: # if key is in dict1 but not in dict 2
                ans_dict[key] = both_dicts[key] 
        else: # if key is not in dict1 but in dict 2
            ans_dict[key] = both_dicts[key]

    return ans_dict   


obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }
print(object_add(obj1, obj2))
# { "x": 4, "y": 12 }


obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }
print(object_add(obj3, obj4))
# { "a": 3, "b": 7, "c": 0, "e": 4 }