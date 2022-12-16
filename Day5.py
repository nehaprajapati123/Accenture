#Functions: 
#built in function 
#user-defined function
#def
#indendation
#parameters(optional)
#
#def add(a,b): # parameters
#    c = a + b
#    return c
# 
#
#print(add(4,6))   
#    
#result = add(4,4,4)#arguments
##
#
#print(result)
#def helloworld():
#    return "Hello World!!!"
#    
#print(helloworld())
#arbitary argument (*)
#def add(a,b):
#    c = a +b
#    print(c)
#    
#add(4,5)
# def student(*name):#arbitary argument/ tuple
#    for i in name:
#        print(i)
# #    print(name[2])
# student("msk","lily","viv","bob")


# def myfunc(name,age,city):  # keyword agument
#    print("The name is",name,
#          "\nThe age is ",age,
#          "\nThe city is ", city)
# myfunc(city = "aaa",name="msk",age=22)


# def myfunc(*name):
#    print("The name is",name[0],
#          "\nThe age is ",name[1],
#          "\nThe city is ", name[2])
         
# myfunc("msk",22,"aaa")

#arbitary keyword arguments: (**kwargs)

# def fun(*name):
#     print(name)
# fun(*[1,2,3,4,5,6,7],"neha","hii")
# fun([1,2,3,4,5,6,7],"neha","hii")     #print all in a single tuple


def myfunc(**kidname): # dictionary
   # print("The fname is ",kidname["fname"],"The last name is ",kidname["lname"],kidname["mname"])
   print(kidname)
myfunc(fname = "msk",mname = "bob",lname= "lily",age = 22)


# def fun(name,collage,*students):
#    print(name)
#    print(collage)
#    print(students)
#    print(type(students))
# fun("lily","hansraj","neha","harry")
# fun(neha="lily",collage = "hansraj","neha","harry")

# def fun(*students,**name):
#    print(students)
#    print(name)
#    print(type(name))
# fun("sagar","mmy",name = "neha")
# fun(name = "neha","sagar","mmy")






#
#default parameter value:
#local, global, nonlocal types of variables 
#
#Global varaible:---declare outside the function
#
#
# x = 5 # global variable
# def area():
#    global x
#    x  = x + 5
#    print("area is",x)
   
# area()
#print(x)
#local variable: --- variables that are created inside the function
#def area():
#    c = "sum" #local variable
#    print(c)
#    
#area()
#
#print(c)
#x = 5#global variable
#
#def area():
#    global x
#    y = 6
#    x = x+y
#    print(x)
#    print(y)
#    
#area()
#Nonlocal Variables:
# def outer():
#    x= "local" # local variable
#    def inner():#nested function
# #        nonlocal x
#        x = "nonlocal"
#        print(x)
#    inner()
#    print(x)
   
# outer()


#Recursive function:---function that calls itself again and again
#factorial
# def factorial(num):
#    if num == 0:
#        return 1
#    else:
#        return num * factorial(num-1)
       
# print("factorial of a number is", factorial(5))

#advantages:
#    
#    1. reduce the number of lines
#    2. readibility
#    3. complex program
#    
#disadvantages:
#  1.   lot of memory and time for execution
#  2. debugging is not easy


#recursive:



#
#def count(n):
#    print(n)
#    if n == 0:
#        return
#    count(n-1)
#        
#        
#count(10)

# min  = lambda a,b,c : a if a < b and a < c else (b if b < c and b < a else c)
    
# print(min(3,2,1))

#Lambda functions:
#syntax: 
#    
#lambda arguments:expression
#    
#sum = lambda a,b:a+b
#
#print(sum(4,5))
#def name(x):
#    return x+x
#    
#lambda x : x+x
# square = lambda x,y : x if(x>y) else y
# #
# print(square(5,7))

#advantages:
#    simple 
#    one line functions
#    
#cons:
#    
#one line
# 
# min  = lambda a,b,c : a if a < b and a < c else (b if b < c and b < a else c)
# print(min(3,2,1))

# while True:
#    value = input("enter you value\t")
#    if value == "Cairo" or value == "quit":
#       break
   