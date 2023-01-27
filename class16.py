# keyword arguments --- are value are provide key =values this way is intergrater recognized the argument by the parameter name. 
# hence in the order in which the argument are passed does not matter 

def average(a=78,b=78):
    print("the average is",(a+b)/2)
  
    average(b=1,a=2)
    