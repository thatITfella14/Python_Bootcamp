myfile = open("Object_and_Data_Structure_Basics/myfile.txt")

file_content = myfile.read() # Read the file ONCE and store it in a variable

print(file_content) # Print the stored variable

myfile.close() # It's also very important to close the file when done

print() # Just to create some space in the output
print() # Just to create some space in the output


# If you try to read the file again, it will return an empty string. That's because the file pointer is at the end of the file. So you'll need to reset it to the beginning if you want to read it again. It can be done by either closing and reopening the file or using the seek() method.

# print(myfile.read()) # Nothing will be printed


# Let's reset the file pointer to the beginning of the file for a new file.

ourfile = open("Object_and_Data_Structure_Basics/test.txt") # file pointer is at the beginning

store_file_content = ourfile.read() # Read the file ONCE and store it in a variable

print(store_file_content) # Print the stored variable

ourfile.seek(0) # Reset the file pointer to the beginning of the file

print() # Just to create some space in the output
print() # Just to create some space in the output

print(store_file_content) # Print the stored variable again

print() # Just to create some space in the output
print() # Just to create some space in the output

# "with" statement automatically takes care of closing the file after the nested block of code

with open("Object_and_Data_Structure_Basics/test_1.txt") as file_1:
    file_data = file_1.read() # Read the file ONCE and store it in a variable
    print(file_data) # Print the stored variable


print() # Just to create some space in the output
print() # Just to create some space in the output


# mode parameter in open() function
# 'r' - Read - Default value. Opens a file for reading, error if the file does not exist
# 'a' - Append - Opens a file for appending, creates the file if it does not exist
# 'w' - Write - Opens a file for writing, creates the file if it does not exist
# 'x' - Create - Creates the specified file, returns an error if the file exists

# with open("object_and_data_structure_basics/new_file.txt", 'r') as f:
#     print(f.read()) # Read mode

# print() # Just to create some space in the output
# print() # Just to create some space in the output

# with(open("Object_and_Data_Structure_Basics/new_file.txt", 'a')) as f:
#     f.write("\nTest 4") # Append mode

with open("Object_and_Data_Structure_Basics/new_file.txt", 'r') as f:
    print(f.read()) # Read mode

print() # Just to create some space in the output
print() # Just to create some space in the output

with open("Object_and_Data_Structure_Basics/random_file.txt", 'w') as f:
    f.write("This is a random file.\nRandom file - Test 2\nRandom file - Test 3") # Write mode

with open("Object_and_Data_Structure_Basics/random_file.txt", 'r') as f:
    print(f.read()) # Read mode