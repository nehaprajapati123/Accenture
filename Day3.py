#Dictionary:
#key:value pairs
#unordered *
#changeable
#duplicates----keys doenst allow duplicates, but values can be duplicates
#{}
#d1 = {}
#print(d1,type(d1))
# from curses.ascii import islower
# from pickle import FALSE


# d1 = {"empname":"msk","age":22,"city":"aaa","active":False}
#
#keys----string,float,int,bool,tuple
#keys are immutable
#
#
#values - anything can be a value
d1 = {"brand":"Ford","model":["hyundai","Maruti"],"age":{"one":1,"two":2}}
#
#print(d1)
#print(d1)
#access values:
#1. square bracket method
#2. get method
#
#print(d1["empname"])
#print(d1.get("active"))
#keys , values, items
#
# print(d1.keys())
# print(d1.values())
# print(d1.items())
#for i in d1.items():
#    print(i)
#
# for i in d1.keys():
#    print(d1[i])
#add an item
#
#d1["fruits"] = "orange"
#print(d1)
#
#d1["age"] = 44
#print(d1)
##
#del d1["active"]
#print(d1)
#d1["dept"] = "aaa"
#print(d1)
#d1["color"] = "orange"
#
#print(d1)
#update
# cars_dict = {"Ford":["Figo","Ecosport"],
#             "Honda":"city",
#             "Hyundai":["Verna","creta"]}
# supercars = {"Ford":"MustangGT",
#              "Lamborghini":"Elemento",
#              "Bugatti":"Veyron"}
#update
#cars_dict.update(supercars)     
#
#print(cars_dict)

# Que:-
Dict1={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
# Print the year that Plato born.
# Change the year from -427 to 428
# “work”:[“Apology”,”Phaedo”,”Republic”,”Symposium”] . add this as new key pair in the above dictionary
Dict2={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
# Add 2 inches to the son's height. And print it.
# Using .items() method generate a list of tuples consisted of each key value pair
# Using get() method print the value of “son’s eyes”
# Clear the whole dictionary


# Ans:-
# print(Dict1["born"])

# Dict1["born"] = 428
# print(Dict1)

# Dict1["work"] = ["Apology”,”Phaedo”,”Republic”,”Symposium"]
# print(Dict1)

# Dict2["son's height"] = Dict2["son's height"] +2
# print(Dict2)

# print(Dict2.items())

# print(Dict2.get("son's eyes"))


# del Dict2
# print(Dict2)


# Sets#####################################################################
#Set :
#unordered
#unindexed
#u cant replace items but you can add new items ,remove items
#{}
#heterogeneous
#doesnt allow duplicates
#empty set 
#s1 = set()
#print(s1,type(s1))
#
#s1 = {"apple","banana","orange",333,45.77,"banana"}
#print(s1)
#print(len(s1))
#print(type(s1))
#for i in s1:
#    print(i)
#add item to a set
#
#s1.add("pomo")
##print(s1)
#
##remove items from set
#
##remove
##discard
#
##s1.remove("apples")
##print(s1)
#
#s1.discard("apples")
#print(s1)
#s1 = {22,33,44,56,66}
#
##if 45 in s1:
##    s1.remove(45)
##else:
##    print("45 doesnt exist in the set")
##    
##print(s1)
#
#s1.discard(45)
#print(s1)
#work with duplicates
#1.update
#2. union
#3.intersection_update---keep only the duplicates
#4. intersection
#5. symmetric_difference_update
#6. symmetric_difference
#s1 = {"abc",40,True,34,"male"}
#
#s2 = {"apple",40,"male","dates"}
#
#s1.update(s2)
#
#s3 = s1.union(s2)
#
#print(s3)
##
#s1 = {22,33,44}
#s2 = {11,22,33}
#
#s1.update(s2)
#
#s3 = s1.union(s2)
#
#print(s1)
#print(s2)
#print(s3)
#
#s1 = {"apple","banana","dates"}
#s2 = {"microsoft","goolge","apple"}
#
##s1.intersection_update(s2)
#
#s3 = s1.intersection(s2)
#
#print(s3)
#combine the sets
#


#union - remove the duplicates and join the set
#intersection-----keep only the duplicates
#symmetric_difference---keep only items that are not duplicate


# s1 = {22,66,77},
# s2 = {11,15,77}
# s3 = s1.union(s2)
#s3 = s1.intersection(s2)
#s3 = s1.symmetric_difference(s2)
# print(s3)



# 1.	Given a Python list, Write a program to add all its elements into a given set.
# sample_set = {"Yellow", "Orange", "Black"}
#      sample_list = ["Blue", "Green", "Red"]
# 2.	Create a new set that only contains common items from both sets.
# S1 = {10,20,30,40,50}
# S2 = {30,40,50,60,70}
# 3.	Update the first set with items that don’t exist in the second set
# set1 = {10, 20, 30} set2 = {20, 40, 50}
# 4.	Check if two sets have any elements in common. If yes, display the common elements
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}



# ans:-1
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# sample_list = set(sample_list)
# sample_set = sample_set.union(sample_list)
# print(sample_set)


# ans2:-
# S1 = {10,20,30,40,50}
# S2 = {30,40,50,60,70}
# s3 = S1.intersection(S2)
# print(s3)


# and3:-
# set1 = {10, 20, 30} 
# set2 = {20, 40, 50}
# set1.symmetric_difference_update(set2)
# print(set1)

# ans4:-
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# set1.intersection_update(set2)
# print(set1)

# que15:-
# Write a program to create a dictionary with cricket players names and their scores in a match. Ask the user to enter the name of a player and return the runs scored by the player
cricket_players = {
    "Dhoni":256,
    "Virat":434,
    "Sachin":747,
    "Rohit":736,
    "Rishabh":283
}

# User = input("Enter Player's name:- ")
# print(cricket_players[User])


# que14:-
# Write a program to find out how many times a particular element is found in a tuple
# tuple = (4,3.4,5,4,8,23,5,9,4,14,4)
# User = int(input("Enter your number:- "))
# count = tuple.count(User)
# print(count)

# ques:-

# Create below 2 sets and try intersection, union, difference_symmetric_difference() 
# Sample input 
#       set1 = {10, 20, 30, 40, 50}
#       set2 = {60, 70, 80, 90, 10}

# ans:-
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# set3 = set1.union(set2)
# print(set3)
# set3 = set1.intersection(set2)
# print(set3)

# set3 = set1.symmetric_difference(set2)
# print(set3)


# Create an empty dictionary and do following operation on it 
#    Add 5 key and values in it 
#    Accept a key from user and remove that key and values from dictionary 
#    Accept a key from user and print the value of that key 
#    Accept all key and values from the dictionary  
# dic = {}
# dic["one"]=1
# dic["two"]=2
# dic["three"]=3
# dic["four"]=4
# dic["five"]=5

# print(dic)

# User  = input("Enter key name:- ")
# if User in dic:
#     del dic[User]
#     print(dic)
# else:
#     print("invalid")

# User  = input("Enter key name:- ")
# print(dic[User])

# for i in dic.items():
#     print(i)



# string:-
str1 = "Hello World!!!!..."
#print(str1)
#print(type(str1))
#print(len(str1))
#for i in range(len(str1)):
#    print(i,str1[i])
#print(str1[5])
#print(str1[5:14])
#print(str1[::-1])
#print(str1[5:14:2])
#print(str1+" welcome")
#
#print(str1.replace("H","J"))
#multiline strings:
#sentence = """Hi how are you
#welcome to python training
#have a nice day python!!!!!"""
#print(sentence.replace("python","java"))
#print(str1.lower())
#print(str1.upper())
#print("hi how are you doing".title())
#print(str1.capitalize())
#strip: ---- remove the whitespace at begining and end
# s = "#Hello!!#"
# print(s.strip('#'))
# print(s.lstrip('#'))
# print(s.rstrip('#'))
# print("HI HOW ARE YOU DOING".title())
# print("HI HOW ARE YOU DOING".capitalize())
# split:convert str into a list of strings
# s = "Hi how #are you doing"

# print(s.split())
#join:will work only for list of strings:
#syntax:
#    
#joining character.join(list name)\
# s = ["Prevention","is","better","than","cure"]

# str2 = " #".join(s)
# print(str2)
#name = "msk"
#age = 22
#
#print("Your name is",name,"and your age is",age)
#
#
#print("your name is {} and your age is {}".format(name,age))
#
#f-string
name = "msk"
age = 23
#print(f"your name is {name} and your age is {age}")
#r-string --- raw string:
# print(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\today\abc.txt")
# print("C:\\Users\\meenakshi.sugumar\\OneDrive - Accenture\\Desktop\\today\\abc.txt")

# que1:-
# Write a program to create a new string made of an input string’s first, middle, and last character.

# Eg: “James” output : “Jms”

# · Hint: String index always starts with 0

# · Use string indexing to get the character present at the given index

# · Get the index of the middle character by dividing string length by 2
# # ans1:-
# word = input("enter your word")
# first = word[0]
# last = word[-1]
# middle =word[round(len(word)/2)]
# print(first+middle+last)


# # ans2:- 
# s1 = "Ault"
# s2 = "Kelly"
# index = round(len(s1)/2)
# lis = []
# for i in s1:
#     lis.append(i)
# lis.insert(index,s2)
# s1 = "".join(lis)
# print(s1)

# # que3:-
# str1 = "WElcome"  #lcomeWE
# low = []
# high = []
# for i in str1:
#     if i.islower():
#         low.append(i)
#     else:
#         high.append(i)
# print("".join(low+high))

# # que4:-
# str1 = "Apple"
# dic = {}
# for i in str1:
#     count = str1.count(i)
#     if i not in dic:
#         dic[i]=count
# print(dic)
    

        
# # que5:-
# str1 = "Emma-is-a-data-scientist"
# str2 = str1.split("-")
# for i in str2:
#     print(i)

# que6:- Accept a string with "#" as a separator. Use the spilt method to display the strings in a list
str = "n#e#h#a"
print(str.split())

#que21:- Write a Python program to display the elements of a list in a reverse order
lis = [1,2,3,4,5,6]
for i in lis[::-1]:
    print(i)

# que22:-Write a program to use the addition operator to:
# - add integers
# - concatenate strings
# - on lists to make a single list

a = 2
b= 3
print(a+b)

a = "Hello"
b = "World"
print(a+b)


a = [1,2,3,4,5]
b= [6,7,8,9,10]
print(a+b)