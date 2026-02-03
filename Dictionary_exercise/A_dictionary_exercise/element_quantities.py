# Dzialwa Nemakonde
# 03 February 2026

#Task:
# Write a function `element_quantities` that accepts a dictionary where:
# - keys are elements
# - values are quantities
# Return a list containing each element repeated according to its quantity.

def element_quantities(dict1):

    list1 = []

    for key in dict1.keys(): # to iterate over the keys of the dictionary 
        for num in dict1.values(): # Accessing the values which are quantities
            list1.append(key) # adding the same key accprding to its quantity
    
    return(list1)


quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']

