# Predicting what each line prints

apple = None
print(apple) # None

apple = 5
print(apple) # 5

apple + 1 # This value is not assigned to anything, since integers are immutable, apple is unchanged
print(apple) # 5

apple += 1
print(apple) # 6

banana = apple
print(banana) # 6

banana = banana / 2 
print(banana) # 3.0

print(apple) # 6 # apple is unaffected because reassignment does not mutate objects, it changes references
