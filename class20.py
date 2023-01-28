# tup =(7,8,)
# print(type(tup),tup)

counteries =(12,465,78,454,44)
temp=list(counteries)
temp.append("russia")
temp.pop(2)
temp[2]="india"
counteries=tuple(temp)
print(counteries)