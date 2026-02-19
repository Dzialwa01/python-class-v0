# Dzialwa Nemakonde
# 16 February 2026

# Creating Objects from a Class

# A class is a blueprint and an object is a real thing created from that blueprint
# E.g. Class -> Design of a house; Object -> Actual house built from that design

# Creating a Simple Class

class Student:
    def greet(self):
        print("Hello from Student class")

# Instance variables
# Thse are variables that belong to a specific object and each object get a copy
# They are usually defined in the __init()__ constructor

#e.g
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# Name and marks are instance variables and each student has their own different value

# Creating an object
s1 = Student() # Student creates an object stored in s1. We now say s1 is an instance of the Student class

s1.greet() # using student class first definition

# Adding attributes to Objects4

class Student:

    def set_name(self, name):
        self.name = name

    def show_name(self):
        print(self.name)    

s1 = Student()
s2 = Student()

s1.set_name ("Alex")
s2.set_name("John")

s1.show_name()
s2.show_name()

# Accessing Attributes Directly
print(s1.name)
print(s2.name)


# Objects allows us to:
# Group data and behaviour together, Create multiple independent instances and write clean and reusable code
