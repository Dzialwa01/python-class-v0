# Dzialwa Nemakonde
# 03 February 2026

# Task:
# Write a function `max_object_value` that accepts a dictionary where:
# - keys are strings
# - values are numbers
# Return a list containing:
# - the key with the highest value
# - the highest value itself

def max_object_value(dict1):

  for key, val in dict1.items():
    if val == max(dict1.values()): # to ensure that we obtain the highest value
      lst = [key, val]
   
  return lst    


print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]