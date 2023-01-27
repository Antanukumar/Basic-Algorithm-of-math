# for loop concept  loop can itrate over the squence of the iterable object in python .itrating of sequence is nothing itration over the string ,list  ,tuple , set 

# dictionary 
# itrating over the string 
name="Antanu"
for i in name:
    # print(i,end=" ")
    # print(i,end=",")
    print(i)
    if (i=="n"):
        print("this is something special")
        
        #itrating over the list
        
        color=["green","blue" ,"white1"]
        for i in color:
            print(i)
            
            for color in color:
                print(color)
                
#range () :---  what it if we are not itrate over1 sequence what if want to use in loop for a spacific number? 
# that time we are use range()


for k in range (100):
    # print(k)
    print(k+1)