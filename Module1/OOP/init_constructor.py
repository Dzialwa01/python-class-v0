# Dzialwa Nemakonde
# 16 February 2026

# The __init__() Constructor

# 1. What is __init__()?
# The __init__() method is a special function that is used to initialise object data.
# In simple words, it sets up values when an object is created. 

# 2. __init__() is called automatically 
# You never call __init__() directly.
# Python calls it automatically when you create an object. 

# 3. Simple Example Without Parameters 
class Student:
    
    def __init__(self):
        print("Student object created")

s1 = Student()

# __init()__ was not called, it ran automatically

# 4. Using Parameters in __init()__
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# self refers to the current object, name and age are parameters. Data is stored inside the object

# 5. Creating Objects with Data

s1 = Student("Ram", 20)
s2 = Student("Sita", 22)
# Each object get its own data

# 6. Accessing Object Data
print(s1.name)
print(s2.age)

# 7. Understanding Parametes Clearly
# Let's break this line
# self.name = name
# It means: left side -> object variable ; right side -> incoming value
# Each object stores its own copy 

# __init()__ matters because with iy, objects are properly initialsed and code becomes clean and organised