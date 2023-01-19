
#? =============================================================================
#* 010 - I/O with Files
#? =============================================================================

myfile = open('Resources\\010_Resources_IO_files\\basic.txt')

print("The basic.txt's file content is: \n{}".format(myfile.read()))

print("Printing out the second time results in an empty string: \n{}".format(myfile.read()))

# ==============================================================================
#* Methods
# ==============================================================================
#* seek()

myfile.seek(0)

print("After resetteing the scope shoulc be work again: \n{}".format(myfile.read()))

#* readlines()

myfile.seek(0)
print("Using readlines(): \n{}".format(myfile.readlines()))
myfile.seek(0)
print("Type of readlines(): \n{}".format(type(myfile.readlines())))

#* close()

myfile.close()

# ==============================================================================
#* With statement
# ==============================================================================

with open('Resources\\010_Resources_IO_files\\basic.txt') as my_new_file:
    new_contents = my_new_file.read()

print("new_contents: {}".format(new_contents))

# ==============================================================================
#* Rights
# ==============================================================================

filePath = "Resources\\010_Resources_IO_files\\basic.txt"

#* "r" - read

with open(filePath, mode = "r") as new_file:
    print("read file with rights: {}".format(new_file.read()))

#* "a" - append

with open(filePath, mode = "a") as f:
    f.write("\nAdded a new line to the file")
with open(filePath, mode = "r") as f:
    print("Printing after added a new line: {}<".format(f.read()))
    
#* "w" - write (overwrite)

with open(filePath, mode = "w") as f:
    f.write("mode = 'w' will overwrite the existing file or create a new")

with open(filePath, mode = "r") as f:
    print("Printing after used mode = 'w': {}<".format(f.read()))
    
#* RESETTING THE FILE

with open(filePath, mode = "w") as f:
    f.write("First line\nSecond line\nThird line")
    
with open(filePath, mode = "r") as f:
    print("After reset file: {}<".format(f.read()))

