# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
l=[1,223,4,5,3]
newl=list(map( square ,l))
print(newl)
