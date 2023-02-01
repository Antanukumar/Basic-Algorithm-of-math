# exception handaling

a=int (input("enter the number :"))
print(f"multible table of the {a}is :")
try:
  for i in range (11):
    print(f'{a} x {i}={int  (a)*i}')
except:
    print("it might be possible")
    print("it work or not")