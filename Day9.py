
#decorators################################################################################

#multithreading
#pandas----more important
#database handling
#Decorators---extra function created for the original code to have some added functionality
#metaprogramming: ---
#decorator function syntax:
#    

# def smart_div(func): #outer fun
#    def inner(a,b):   #inner fun
#        if a < b:
#            a,b = b,a
#        return func(a,b) #return inner
#    return inner         #return outer
       
# @smart_div       
# def div(a,b):
#    print(a/b)
   
# div(5,50)


#def splitstring_decorator(func):
#    def inner():
#        a = func()
#        result = a.split()
#        return result
#    return inner
#    
# def uppercase_decorator(func):
#    def inner():
#        a = func()
#        result = a.upper()
#        return result
#    return inner
# #    
# #@splitstring_decorator
# @uppercase_decorator
# def myfunc():
#    return "Hello there"
# #    
# print(myfunc())
# #
#
#
#@uppercase_decorator
#def hisfunc():
#    return "Welcome"
#def multiply_by_num(num):   
#    def multiply(func):
#        def inner(a,b):
#            return func(a,b)*num
#        return inner
#    return multiply
#        
#
#
#@multiply_by_num(15)#parametrizing decorator
#def add(a,b):
#    return a+b
#    
#print(add(3,4))
#@multiply_by_two
#def subtract(a,b):
#    return a-b
#    
#print(subtract(10,5))

#Multithreading:#######################################################################
#threading module ---- inbuilt
#process
#multiprocess-----parallellsim---2 sales person
#thread
#lightweight process
#a smalles executable program in the cpu
#a sub process
#thread life cycle
#thread id
#stack pointer ---memory location
#start
#run
#wait
#dead
#demon --- Unfinished thread
#multithread ---- concurrency----1 sales person(waiting)
#parallellism
#concurrency
#Multithreading in python:
#from threading import Thread

# from threading import Thread
# from time import sleep
# class Hello(Thread):
#     def run(self):
#         for i in range(2):
#             print("Hello")
#             sleep(1)
# class Hi(Thread):
#     def run(self):
#         for i in range(2):
#             print("Hi")
#             sleep(1)
# t1 = Hello()
# t2 = Hi()
# t1.start() ## why start?
# sleep(0.2)
# t2.start()



#Pandas : 
#pandas library:
#    
##data analytics
##data statistics
##AI & ML
#    
#2 different types of data structure:
#    
#    1. Pandas Series --- 1D dimension
#    2. pandas  DataFrame --- 2D 
#pandas series
#
# import pandas as pd
# # empty panda series
# l1 = [2,3,4,6,7,8,0]
# s1 = pd.Series(l1)
# print(s1)
# print(type(s1))
##
##t1 = tuple(l1)
##print(t1)
##print(type(t1))
#
#type()
#dtype keyword
#l1 = [2,3,4,6,7,8]
#
d1 = {"name":"msk","age":22,"city":"aa"}

s1 = pd.Series(d1)

print(s1)
#t1 = (3,44,55,66,88,99,9900,3,3,3,3,3,99)
#s3 = pd.Series(t1)
#print(s3)
#print(s3+2)
#for i in s3:
#    for j in range(10):
#        s3 = s3+j
#        
#print(s3)
##
##print(s3.count())
#
#print(s3.value_counts())
#print(s3)
#
#print(s3.max())
#print(s3.min())
#
#print(s3.mean())#average
#del s3
#print(s3)
#panda series is immutable:
#
#print(s3[4])
#
#print(s3[2:5])


    
#Pandas DataFrame
# import pandas as pd
#
#df = pd.DataFrame(index = [1,2,3,4,5],columns = ["Name","Age","City"])
#
#print(df)
#from list
#
#l1 = [33,44,55,66,77,88,44]
#
#df = pd.DataFrame(l1,columns = ["marks"],index =["eng","tamil","physics","maths","science","chemistry","java"])
#
#print(df)
#from dictionary
#d1 = {"name":["msk","lily","bob","parr"],
#      "age":[22,33,44,23],
#"city":["aaa","bbb","ccc","ddd"]}
#
#df = pd.DataFrame(d1,index = ["A","B","C","D"])
#
#print(df)
#read_csv =---- csv file to dataframe
#read_excel --- excel file to dataframe
#convert excel to df
# import pandas as pd
# df = pd.read_excel(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\test_df.xlsx")
#print(df)
#
#print(type(df))
#head and Tail function:
#
#print(df.head(6))
#
#print(df.tail(2))
#indexing and slicing:
#how to select one particulat column or row from the df:
#print(df)
#select one column: syntax: df[column name]
#print(type(df["Empid"]))
#
#df1 = pd.read_csv("sample2.csv")
#
#print(df1.tail())
#print(df["Age"])
#loc----using column names & iloc ---column index
#print(df.loc[3:6,["Age","Dept","Name"]])
#print(df.iloc[3:6,1:3])
#filtering :
#print(df)
#syntax: df[condition]
#print(df[df["Dept"]=="IT"])
#
#print(df[df["Dept"] == "HR"])
#print(df[df["Age"]>25])
#syntax: df[()&()]
#print(df[(df["Dept"]=="IT") | (df["Age"]>25)])
#
#print(df[(df["Dept"]=="IT") & (df["Age"]>25)])
#print(~(df[df["Dept"]=="IT"]))
