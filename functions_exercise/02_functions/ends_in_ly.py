# Write a function `ends_in_ly` that accepts a string.
# Return True if the string ends with "ly".
# Otherwise, return False.

def ends_in_ly(word):

    return word[-2:] == 'ly'


print(ends_in_ly("pretty"))      # False
print(ends_in_ly("instant"))     # False
print(ends_in_ly("analytic"))    # False
print(ends_in_ly("timidly"))     # True
print(ends_in_ly("fly"))         # True
print(ends_in_ly("gallantly"))   # True

