# Dzialwa Nemakonde
# 17 February 2026

# The open() Function
# To read a file, we first need to open it and this is doen using the open() funtion
# Syntax: open("filename", "mode")

# Read modes (Basic)
# We mainly use "r" -> read mode. NB the file must already exist

# Create a simple file
# Before reading we are going to create a file named data.txt

# Reading the entire File
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# The above code opens the file, reads all the content, stores it in a variable then prints it. 

# Why is closing a file important?
# It frees system resources, Prevents data corruption and its also a good programming practices

# Reading line by line
# we use the readline() method to read the first line of the file
file = open("data.txt", "r")
line = file.readline()
print(line)
file.close()

# Reading all lines as a list
file = open("data.txt", 'r')
lines = file.readlines()
print(lines)
file.close()
# print out a list where the elements are each line of the file