# Dzialwa Nemakonde
# 20 January 2026

# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

def no_ohs(text):
 
 for i in text:
  
  ch = "o"

  if i.lower() != ch: # ensuring it only print letters which are not o's
   print(i) 

# Example:
 no_ohs("code")
# c
# d
# e


