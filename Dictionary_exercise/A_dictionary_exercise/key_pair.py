# Dzialwa Nemakonde
# 03 February 2026

# Write a function `key_pair` that accepts:
# - two dictionaries
# - a key string
# Return a list containing the values for the given key from both dictionaries.

def key_pair(dict1, dict2, key):
    
    lst = [] 

    lst.append(dict1[key])
    lst.append(dict2[key])

    return lst

cat1 = {"name":"jinkee","breed":"calico" }
cat2 = {"name":"garfield","breed":"red tabby" }

print(key_pair(cat1, cat2,"breed"))
# ['calico', 'red tabby']

print(key_pair(cat1, cat2,"name"))
# ['jinkee', 'garfield']

