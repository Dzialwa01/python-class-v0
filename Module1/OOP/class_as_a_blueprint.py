# Dzialwa Nemakonde
# 16 February 2026

# Class as a Blueprint

# Think of a class like a plan.
# e.g.:
# Class -> Student
# Object -> Ram, Sita, Hari
# All students share the same structure, but each has different data. 

# 2. Creating a Class in Python
# To create a class, we use keyword "class". 
# Basic syntax:

class Classname:
    pass # Do nothing for now

# 3. Class Naming Convention
# Class names should follow: PascalCase, First letter capitalised and Meaningful names.
# Examples:

# class Student:
# class Car:
# class BankAccount:

# Bad examples:
# class student:
# class myclass:
 
# A Simple Class Example
# Let's create a simple Student class. 

class Student:
    pass

# Now, let's create an object from this class.

s1 = Student()
s2 = Student()

# Student is the class. s1 and s2 are objects. 

# 5. Object from the Same Class
# Even though both objects come from the same class, they are different objects.
print(s1)
print(s2)
# Each object has its own identity. 

## Classes allow us to Group  related data and behaviour, create multiple object easily and Model real-world entities.