# Predicted results in comments alongside

print(False)    # False 
print(not True) # False
print(not False) # True
print(not not True) # True

# with the expression and, both should be true in order for it to be true otherwise false

print(False and False) # False
print(False and True) # False
print(True and False) # False
print(True and True) # True

# with the expression or, one should be true in order for it to return true

print(False or False) # False
print(False or True) # True
print(True or False) # True
print(True or True) # True

print((not False) or False) # True
print(False or (True and True)) # True
print(False or not (True and True)) # False
print((not True) and (False or True)) # False

