# Dzialwa Nemakonde
# 18 February 2026

# WHat is a module?
# A module is a pythoon file that contains: varibales, functions and classes
# Any file ending with .py is a module

# Modules are used for:
# Code reusability, better organisation, easier maintenance, team collaboration and cleaner projects. 
# The rule is one module should have one responsibility.

# Importing a module (Basic)
# we use the import key word to import a a module. E.g:
import math
print(math.sqrt(16))
# math -> module name ; sqrt -> function inside module

# we can even import specific items in the module
from math import sqrt, pow
print(sqrt(25))
print(pow(2,3))

# We import using an alias
import math as m
print(m.pi)

# Importing everything in a module is not recommended.
# This is because it pollutes namesapce, it becomes hard to debug, and it overrides variables.

# Module Search path(sys.path)
import sys
print(sys.path)
# python searches modules in current directory, standard library and installed packages

# Standard Library Modules (Must Know)
# math -> for math functions and constants
# random -> for generating random numbers
# datetime 
# os
# sys