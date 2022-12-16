# control statements and loops:
#1. if
#2. if else
#3. if elif else
#
#4. While loops
#5.for loops
#If condition ----- code will execute only if the condition is true
#Indendation: ---- whitespace at the begininig of the line 
#a = 33
#b = 33
#if a > b:
#   print("a is greater")
#elif a==b:
#    print("Both are equal")
#else:
#    print("b is greater")
# import random
#
#die_roll = random.randint(1,6)
#print(die_roll)
#and not or --- logical gates 
#if die_roll == 2 or die_roll == 4 or die_roll == 6:
#    print("The number is even")
#elif die_roll == 3 or die_roll == 5:
#    print("The number is odd")
#else:
#    print("The number is one")
#
#n = int(input("Enter any number:"))
#
#if n>0:
#    print("Number is positive")
#elif n < 0:
#    print("The number is negative")
#else:
#    print("The number is zero")



# que
#Get any number as input from user and check the given number is odd or even
#Hint : to check even the condition is  :
#n % 2 == 0  
#Get a number as input and check if the number is divisible by 5 or not
#3. Get three numbers from         users and find the biggest number among them and print it 

#ans1:-
# num = int(input("enter the number:- "))
# if num %2 == 0:
#     print("even")
# else:
#     print("odd")

# #ans2:-
# num = int(input("enter number:- "))
# if num%5 == 0:
#     print("divisible")
# else:
#     print("not divisible")
    
# #ans3:-
# num1 = int(input("enter number1:- "))
# num2 = int(input("enter number2:- "))
# num3 = int(input("enter number3:- "))
# if num1 > num2 and num1>num3:
#     print(num1,"is greater")
# elif num2> num1 and num2>num3:
#     print(num2,"is greater")
# else:
#     print(num3,"is greater")
    
print("a")
#For Loop:
#with range function
#without range function:
#for i in range(2,30):
#    if i%2 != 0:
#        print(i)
#    
#for i in range(30,2,-2):
#    print(i)
#sum of n numbers using for loop :   
#n = int(input("Enter any number :"))
#sum = 0
#for i in range(0,10):
#    sum += i
#    print(sum)

# Data structure
#Data Structures:
#collections:
#storing multiple values in single variable
#4 inbuilt collextions:
#1. list
#2. tuples
#3. set
#4. dictionary
#common activity:
#create 
#add items
#replace
#remove 
#access
#delete
#List:
#used to store multiple values in single variable
#one of 4 inbuilt data structure
#heterogeneous---allows all datatypes in single 
#ordered
#changeable
#allow duplicates
#mutable
#follows indexing
#[]
list1 = ["Mercury",3456,34.4664,False,3456]
#print(list1[0])
#print(list1[1])
#print(list1[2])
#print(list1[3])
#print(list1[4])
#for i in list1:
#    print(i)
#len() -- length function:
#print(len(list1))
#
#n  = len(list1)
#
#for i in range(5):
#    print(i,list1[i])
#
#in / not in
fruits = ["apple","banana","cherry","dates","mango","kiwi","orange","pomo"]
#print(fruits)
#print(len(fruits))
#print(type(fruits))
#print(fruits[2])
#print("apple" not in fruits)
#index:
#print(fruits.index("kiwi"))
#add items to the list
#append---add item to the last
#insert --- add item anywhere
#fruits.append("papaya")
#
#print(fruits)
#
#fruits.insert(2,"strawberry")
#print(fruits)
#replace
#
#fruits[2] = "papaya"
#print(fruits)
#slicing:
#print(fruits[1:5:])
#print(fruits[3:6])
#print(fruits[:6])
#print(fruits[4:])
#print(fruits[2:7:2])
#print(fruits[::1])
#print(fruits[::-2])
#print(fruits[:])
#remove
#remove ---- remove by item name
#pop ---- remove by index number
#fruits.remove("orange")
#print(fruits)
#fruits.pop(3)
#print(fruits)
#
#fruits.pop()
#print(fruits)
#
#del fruits[3]
#print(fruits)
#fruits.clear()
#print(fruits)
#
#del fruits
#print(fruits)


# questions
# 1.	Create a list with 10 numbers and  Display numbers from a list using  a for   loop. 
# 2.	Create a list and print in reverse order using slicing
# 3.	Create two list and join two list using + operator
# 4.	Create a list and add a new item in the 4th index
# 5.	Write a program to find value 20 in a list. If 20 is present in the list replace it with 200. 


#que1:-
#num = [1,2,3,4,5,6,7,8,9,10]
#for i in num:
#    print(i)

#que2:-
#num = [1,2,3,4,5,6,7,8,9,10]
#print(num[::-1])   

#que3:-
#num = [1,2,3,4,5,6,7,8,9,10]
#num2= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#print(num + num2)
#
#    
#que4:-
#num = [1,2,3,4,5,6,7,8,9,10]
#num.insert(4,"Neha")
#print(num)

#que5:-
#num = [1,2,3,4,5,6,7,8,9,10,20]
#if 20 in num:
#    index = num.index(20)
#    num[index]= 200
#    print(num)


#Tuple
#heterogenous
#ordered
#unchangeable/immutable
#()
#allow duplicates
t1 = ("apple","banana",2344,45.687)
#print(t1[0])
#print(t1[1])
#print(t1[2])
#print(t1[3])
#
#print(t1[1:3])
#
#t1[1] = "orange"
#del t1
#print(t1)
#l1 = list(t1)
#print(l1)
#l1.append("orange")
#t1 = tuple(l1)
#print(t1)
#t1 = ()
#print(t1,type(t1))
#
#t1 = (5,)
#t2 = (5.34,)
#t3 = ("msk",)
#t4 = (False,)
#t5 = ([1,2,3],)
#t6 = ()
#l1 =[3]
#
#print(type(t1))
#print(type(t2))
#print(type(t3))
#print(type(t4))
#print(type(t5))
#print(type(t6))
#
#print(type(l1))
#a = 5,6,7
#print(type(a))

# list = [1,2,3,4,5]
# list1 =[]
# for i in list:
#     cube = i**3
#     list1.append(cube)
# print(list1)



# list = [[1,2,3,4,5],[6,7,8,9,10]]
# list1=[]
# for i in list:
#     for j in i:
#         list1.append(j)
# print(list1)

# list =[]
# for yr in range(2000,2100,4):
#     list.append(yr)
# print(list)
