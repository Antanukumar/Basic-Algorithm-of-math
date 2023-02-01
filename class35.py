#The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object. The enumerate() function adds a counter as the key of the enumerate object.


marks=(45,44,74,45454,78)
for index,marks in enumerate(marks):
    print(marks)
    if(index==3):
        print("aaaaa")
    