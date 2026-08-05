import random


x=10
#print(type(x))



#Complex Type
c=1j
#print(c)
#print(type(c))

#Tuple Type
tup=("apple", "banana", "cherry")
#print(tup)
#print(type(tup))

#Range Type
ra=range(6)
#print(ra)
#print(type(ra))


#dict Type
dic= {"name" : "John", "age" : 36}
#print(dic)
#print(type(dic))


#set Type
se= {"apple", "banana", "cherry"}
#print(se)
#print(type(se))


#frozenset Type
frse= frozenset({"apple", "banana", "cherry"})
#print(frse)
#print(type(frse))


#byte Type
by=b"Hello"
#print(by)
#print(type(by))



#bytearray Type
byarr= bytearray(5)
#print(byarr)
#print(type(byarr))


#memoryview Type
memvie= memoryview(bytes(5))
#print(memvie)
#print(type(memvie))


########-------------------------------------------------------
x = str("Hello World") #when we want to specify data type

#how to convert

x=10 #this is int type

a=float(x) #convert from int to float

#pay attention that we can use int() float() etc, to define data type and convert datatype and cast data type:
#int(2.5) cast to int result=2

# print(random.randrange(1, 10)) # to make random numbers you must use this code and add  "import random" library

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("free" in txt) #check if "free" exist in text

# txt = "The best things in life are free!"
# print("free" not in txt) #check if "free" doess not exist in text

# b = "Hello, World!"
# print(b[2:8])  # slicing  string from index 2 to 7 (8 is not included)
# print(b[:5]) #from 0
# print(b[2:]) #from 2 to end 
# print(b[-5:-2]) #it works onplace above code works on index ,-5 means 5th from end and -2 means 2nd from end, so it will slice from 5th to 2nd from end

a = " Hello, World! "
#print(a.strip()) #The strip() method removes any whitespace from the beginning or the end:



#number=36
# print(f"your number is {number}") #we use 'f' for combining string and number ,etc

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

#txt = "We are the so-called \"Vikings\" from the north." # we use \ to use double quotes inside string

# \' 	Single Quote 	
# \\ 	Backslash 	
# \n 	New Line 	
# \r 	Carriage Return 	
# \t 	Tab 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value


