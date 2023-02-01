#  What is local and global variables in Python?
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x=10
def func():
    global x
    x=4
    y=45
    print(y)
    
    func()
    print(x)
