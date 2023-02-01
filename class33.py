# Exception handling is the process to unwanted or unexpected events when computer program run .    
#Exception handling deals with these events to avoid the program or system crashing     
#and without this process exception would  disrupt the normal  operating on programm

# exception handaling

a=int (input("enter the number :"))
print(f"multible table of the {a}is :")
try:
  for i in range (11):
    print(f'{a} x {i}={int  (a)*i}')
except:
    print("it might be possible")
    print("it work or not")