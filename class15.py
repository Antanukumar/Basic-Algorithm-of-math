# default function argument the values while creating .this way the function assumes a default  values even if a values is not provides in the function call for the argument

def average(a=78,b=78):
    print("the average is",(a+b)/2)
    # average(4,8)
    # average()
    # average(1,2)
    average(a=9)