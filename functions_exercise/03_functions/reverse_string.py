# Extra no:1 
# Write a function reverse_string(text) that returns the reversed string.

# Done with string slicing
# def reverse_string(str1):  
#     return str1[::-1]

# Done with recursion
def reverse_string(str1, a = 0):

    if len(str1) == 0:
        return ""
    else:
         a = len(str1)
         return str1[-1] + reverse_string(str1[:a-1], 0)


    
print(reverse_string("hello"))   # olleh
print(reverse_string("Python"))  # nohtyP

