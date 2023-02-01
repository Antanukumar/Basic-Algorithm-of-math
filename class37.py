# What is Python file handling?
# File Handling

# The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode. There are four different methods (modes) for opening a file: "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
# f = open(filename, mode)
# Where the following mode is supported:

# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
#  r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.

f=open('file.text','r')
text=f.read()
print(text)
f.close()