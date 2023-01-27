def average(*number1):
    sum=0
    for i in number1 :
        sum =sum +i
    return sum /len(number1)
c = average(1,45,8)
print(c)