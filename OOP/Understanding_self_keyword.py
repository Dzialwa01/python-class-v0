# Dzialwa Nemakonde
# 16 February 2026 

# Understanding the self Keyword

# In python, self is the reference to the current object. 
# In simple words: self mean "this object."
# So whenever we create an object from a class, self refers to that specific object.

# Starting off with a simple class

class Student:
    def greet(self):
        print("Hello student.")

s1 = Student()
s1.greet()

# Internally python does this: Student.greet(s1)
# THe s1 is passed automatically and it becomes self

# We need self because each object has its own data
# e.g.
class Student:
    
    def set_name(self, name):
        self.name = name

    def show_name(self):
        print(self.name) 

# creating two objects
s1 = Student()
s2 = Student()

s1.set_name("Alex")
s2.set_name("John")

s1.show_name()
s2.show_name()

# self.name is a variable inside the object. Each object has its own copy.
# This is why self is important because it keeps data separate for each object.

# When we assign variables, e.g name, we do not say name =; we say self.name =
# This is because without self, python will not know which object the variable belongs to. 
# self can be renamed, but always use it as it the Python convention

# Analogy
# Think of a class as a form. So each object is a filled form.
# self means this particular form, so self.name = name written on this form

# Summary:
# self refers to the current object
# Python passes it automatically
# It allows objects to store their own data
# self avoids data conflicts between objects