# Praticing how loops work and how thier syntax.

# Snippet 1

print("hello")

# The range function has three arguments: range(start:stop:step)
# i is assigned to the start, then the condition i < stop is checked. If true the loop executes, start is then increased by step and the condition is checked again until it is false the loop terminates
# the step determines how the start changes from one iteration to the next
# Loop first completes all iterations then the program moves to the next line of code


for i in range(5): 
    print("code")

print("goodbye")


# Snippet 2

print("hi")

for i in range(3, 8): # Loops start from 3 and ends at 7
    print("program")
    print(i)

print("bye")

# Snippet 3

def foo():

     # The loop starts with num == 10, as each iteration passes, num decreases by 2 as step is -2. and condition checked is now start > stop
    for num in range(10, 0, -2): 
        print(num)

print("begin")
foo()
print("end")
foo()


# Snippet 4

word = "street"

for i in range(len(word)): # prints each letter and its index one at a time with each iteration
    print(i)
    print(word[i])


# Snippet 5    

total = 0

for i in range(1, 5):
    total += i # adds the value of i to total, incrementing it at each iteration 
    print(total)

print("grand total:", total) # the grand total is printed at the end of the iteration



