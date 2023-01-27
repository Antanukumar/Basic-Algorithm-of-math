#  variable argument and key argument function


def average(*number1):
    sum=0
    for i in number1 :
        sum =sum +i
        print ("average number:",sum /len(number1)) 
        average(1,45,8)