# Dzialwa Nemakonde
# 17 February 2026

# Writing Data to Files

# 1. Write vs Append (NB)

#  There are two main ways to write data to a file:

## Write Mode ("w"): This creates a new file, overwrites the an existing file and deletes old content. 
# Ensure you do not open a file with this mode with data you still want to use.

## Append Mode("a"): Adds data at end, keeps existing content. It is safer for logs and records.

# 2. Writing Data using the write mode:
# Example
file = open("output.txt", "w")
file.write("Hello Python\n")
file.write("File handling is useful\n")
file.close()

# 3. Appending Data to a file
# Example
file = open("output.txt", "a")
file.write("Learning step by step\n")
file.close()

# NB : Even when writing to the file, it still needs to be closed as this ensures that the data is saved properly andd no file corruption.

# Example Program: Save Student Name

name = input("Enter student name: ")

file = open("students.txt", "a")
file.write(name + "\n")
file.close()