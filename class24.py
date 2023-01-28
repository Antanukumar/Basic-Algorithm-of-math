# python recursive function  a function call other function it is even posible for the function to call itself .these type of construction is called recursion function 

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    print(factorial(5))
    