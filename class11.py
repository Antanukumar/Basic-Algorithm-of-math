 # match case  statemnt programm in python x=2

x= int(input("enter the number :"))
match x:
    case 0:
        print("x is zero")
        
    case 4:
            
        print("x is 4")
    case _ if x==20:   # this is match concept follow bye switch statement 
        print("x")
    case _ if x!=90:
        print("if x is not equal to 90")
    case _ :
        print("y")
        