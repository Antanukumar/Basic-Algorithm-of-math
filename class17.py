# required argument === in case we dosn't pass the argument with a key=values syntax ,the it is necessary to pass the argument in the correct positional 
## order is corrct order and the number of argument passed should match with actual function defnation 

def average(a,b,c=78):
    print("the average is",(a+b+c)/2)
  
    average(12,2)
    
    