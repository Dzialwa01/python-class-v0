# Dzialwa Nemakonde
# 17 February 2026

# Introduction to File Handling

# Why do file matter?
# When we work with data in our programs, once the program stop, the data is gone
# So files help us to; store data permanently, read saved data later, ans share data between programs.

# Real life Examples:
# Saving user details; Storing results of students, writing logs. reading configuration files. 

# What is file handling?
# File handling means:
# Opening a file; Reading data from a file, Writing data to a file and closing a file

# Reading vs Writing files
# In files there are two main operations:
# Reading a file: Getting data from a file; file must already exist
# Writing to a file: Putting data into a file; Can create a new file; Can overwrite an existing file

# E.g
file = open("data.txt", "r")
# This means: Open data.txt in read mode

# What happens if file doesn't exist?
# Read mode -> gives an error
# Write mode -> creates a new file