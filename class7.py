# string method in python  are immutable 
# python provide a set of build in method that can be used to alter and modified  the string 


#upper method in used to convert upper case string upper():


str1="AbcdjijhD"
print(str1.upper())

# lower method is used to  convert lower case string lower ():


a="Antanu"
print(a.lower())

#strip() method used to remove any white space before and after string 

a1="silver spoon1"
print(a1.strip())


# rstrip()  is used trilling character removed just like :--!!!!!!!!!!

A1="ANtanu!!!!"
print(A1.rstrip("!"))


#replace () method are replaced all occurance of string with another string 

a2="silver Spoon 1"
print(a2.replace("s","o"))

# split() is genaraly used in  convert sstring into list form

print(a2.split(" "))

#capitalize(): is used to convert method turn into first character is used to convert uppercase and rest of character convert into lower case 

print(a2.capitalize())

#center() method align the string to the center as per parameter given by the user.


str2="welcome to console 1"
print(len(str2))
print(len(str2.center(50)))


#count() is used to method return the number of time of given values the occure with in giving string

print(str2.count("o"))

#endwith():-- method are used to end with given values if yes the values given true and else its false.

print(str2.endswith("to"))
print(str2.endswith("1"))

#find() :---- method find the first occurance of of the given values and return the index where is persent .the given values is absent return value is -1.


b2="hii i am the coder of python1"
print(b2.find ("am"))
print(b2.index ("am"))

# isalum () :--- method return true only if the entier string only consist of A-z ,a-z ,0-9 if any character are punchutation is return value is false

v3="helloeveryone11"
print(v3.isalnum())

#swapcase method are used to upper case convert lowercase and lower case convert upper case

print(v3.swapcase())


#title() :-- title method are used to conver character in title form in string 

print(v3.title())