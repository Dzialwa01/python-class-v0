# Dzialwa Nemakonde
# 17 February 2026

# Using the with Statement

# Problem with manual close()
# So far we have close the file manually using file.close()
# This works, however, if an error happens before close(), the file may remain open.
# This may cause memory issues, file corruption and it is a bad programming habit.

# What is the with statement?
# The with statement opens the file, handles it safely and automatically closes the file, even if an error occurs.
# So we do not need file.close() anymore

# Reading a file using with
with open("data.txt", "r") as file:
    content = file.read()
print(content)

# There is no close() call as python closes the file automatically. 
# The code is shorter and much safer

# Writing to a File Using with
with open("output2.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Using the with statement\n")

# Append Mode using with
with open("output2.txt", "a") as file:
    file.write("Learning best practices\n")


## The with statement gives us automatic file closing, cleaner syntax, safer code and professional coding style
## this is why it is the best practice and its actually used by real python developers
