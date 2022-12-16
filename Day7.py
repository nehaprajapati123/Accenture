#Encapsulation: from subprocess import call

class BankAccount:
    # bank_name = "CCCC"
    # interest_Rate = 8.00
    def __init__(self,acc_num,acc_name,balance):
        self.__acc_num = acc_num
        self.__acc_name = acc_name
        self.__balance = balance

    def get_acc_name(self):
        return self.__acc_name
    def get_acc_num(self):
        return self.__acc_num

    def get_balance(self):
        return self.__balance

    def set_balance(self,new_balance):
        self.__balance = new_balance
        
    def add_money(self,deposit_amt):
        self.__balance += deposit_amt

        print("The amount is deposited, your new balance is",self.__balance)
    def withdraw_money(self,withdraw_amt):
        if withdraw_amt <= self.__balance:
            self.__balance -= withdraw_amt
            print("The amount withdrawn, final balance is",self.__balance)
        else:
            print("Insufficient balance")
millionaire = BankAccount(1105,"Jeff",1000000000)
# print(millionaire.acc_name,millionaire.acc_num,millionaire.balance)
#millionaire.add_money(500)
#
#millionaire.withdraw_money(198700000000000)
# millionaire.acc_name = "msk"
#print(millionaire.acc_name,millionaire.acc_num,millionaire.balance) 
#
#millionaire.add_money(12344)
#millionaire.withdraw_money(234567)
#
#print(millionaire.__balance)
#millionaire.__acc_name = "jeff"
#getter and setter methods
# print(millionaire.get_acc_name())
# print(millionaire.get_acc_num())
print(millionaire.get_balance())
#
millionaire.set_balance(1000)
#
print(millionaire.get_balance())


# Create a class mobile with 3 instance variables :brand , model, price
# class Mobile:
#     def __init__(self,brand,model,price):
#         self.__brand = brand
#         self.__model = model
#         self.__price = price

# Create two functions  : call and discount
   
#     def call(self,mobile_number):
#         print("calling to ", mobile_number)

    
#     def get_brand(self):
#         return self.__brand
#     def get_model(self):
#         return self.__model
#     def get_price(self):
#         return self.__price

#     def set_brand(self,brand):
#         self.__brand = brand
#     def set_model(self,model):
#         self.__model = model
#     def set_price(self,price):
#         self.__price = price

#     def set_discount(self,discount_amt):
#         self.__price -= discount_amt

# # # Print the variable values and run the functions
# Mobile_info  = Mobile("abc","xyz",150000)

# Mobile_info.call(78769)

# # Make the variables private. Use get and set functions to change and print the values of private variables
# print(Mobile_info.get_brand())
# print(Mobile_info.get_model())

# Mobile_info.set_price(5000)
# print(Mobile_info.get_price())





#polymorphism: - greek word##############################################################
#
#poly  ---- many/ multiple
#
#morph --- forms/ shapes 
#
#
#one thing can take multiple shapes or forms
#
#Water: 

#operator overloading

#method overloading
#method overriding


print(5+6)

print("5"+"6")
#
#print([1,2,4]+[5,6,7])
#Magic methods: __ __, __init__, __dict__
# + = __add__()
#a + b
#
#+ is operator
#a,b is called as operands
#print(type(5))
print(5+6)

print(int.__add__(5,6))

#
print("5"+"6")
#
print(str.__add__('5','6'))

#
print(list.__add__([1,2,3],[5,6,7]))
# operator overloading example

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(s1,s2):
#         final_m1 = s1.m1 + s2.m1
#         final_m2 = s1.m2 + s2.m2
#         object1 = Student(final_m1,final_m2)
#         return object1
# s1 = Student(66,88)
# s2 = Student(77,84)
# s4 = s1 + s2
# print(s4.m1,s4.m2)
# print(type(s4))




# Text File Handling :##############################################################
#csv--comma separated values
#excel--table format
#text file

#open()
#write()
#read()
#create()
#syntax:
#    
#open(filename,mode)
#mode
#-r- read -open the file to read. 
#-w- it will open the file to overwrite
#-a- it will add some new data to the file
#-x- it will create a new file.
#-b- binary images
#-t- text
#read
#readline
#readlines
#
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc1.txt",'r')
#f.close()
#print(f.read(4))
#print(f.readline())
#print(f.readline())
#print(f.readlines())
#read particular line from the doc
#data = f.readlines()
#print(data[14])
#last five lines of the file
#
#for i in range(1,6):
#    print(data[i*-1])
#Write and append
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc1.txt",'a')
#f.write("\nHi i am the newly added line")
#f.close()


#how to append in the middle of a file:
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc1.txt",'r')
#data = f.readlines()
#print(data)
#f.close()
#
#data.insert(7,"Hi I am the newly inserted line\n")
#newdata = "".join(data)
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc1.txt",'w')
#f.write(newdata)
#f.close()
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\msk.txt",'w')
#f.write("Hello All")



#
#import os
#os.remove(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Documents\Python Scripts\test")
#
#
##remove folder along with file
#
#import shutil
#shutil.rmtree("test")



# que12:-Write a program to know whether a sub string is there in the main string or not. 

# main_str = input("enter a main string\t")
# sub_str = input("enter a sub string\t")
# if sub_str in main_str:
#     print("yes present")
# else:
#     print("not present")

# # que13:-Write a program to display all the positions of a sub string in a main string

# main_str = input("enter a main string\t")
# sub_str = input("enter a sub string\t")
# if sub_str in main_str:
#     i=0
#     while i<len(main_str):
#         if main_str[i] == sub_str:
#             print(i)
#         i+=1
# else:
#     print("not present")   
        

# # ques17:-Create a simple calculator using functions
# num1 = int(input("enter num1\t"))
# operator = input("enter operator\t")
# num2 = int(input("enter num2\t"))

# def calculator(num1,num2,operator):
#     if operator == "+":
#         print(num1+num2)
#     elif operator == "-":
#         print(num1-num2)
#     elif operator == "*":
#         print(num1*num2)
#     elif operator == "/":
#         print(num1/num2)
#     else:
#         print("you choose a invalid operator")
# calculator(num1,num2,operator)

# que18:-Write a program to define a student class that has the following attributes:
# - Name
# - Student ID
# - Marks
# The class must have a method to display the details.
# Also create an object that calls the method to display the details

# class Student:
#     def __init__(self,name,student_ID,Marks):
#         self.name = name 
#         self.student_ID = student_ID 
#         self.Marks = Marks 
#     def Details(self):
#         print(self.name,self.student_ID,self.Marks)
# Info = Student("NSP",2130,89)
# Info.Details()

# # que19:-Write a program to explain the difference between a local and global variable

# x = 8
# def fun():
#     print(x) # this will print becz its a global var and can execute globally + locally
#     y = 7
#     print(y) # local variabe execute only localy only
# fun()
# print(x) 
# print(y) #this will through error its a local var.


# que20:-Write a lambda function:
# - to calculate the sum of two numbers
# - that returns the square of a number
# - that returns the even numbers in a list

# sum = lambda x,y: x+y
# print(sum(1,2))

# square = lambda a: a**2
# print(square(int(input("enter the number"))))

# even = lambda x:[i for i in range(1,x) if i%2 == 0]
# print(even(10))

# que26:-Write a program to :
# - Read the data from an existing file
# - Append data to the file
# - Display the data with newly appended data

# file = open("file","x")
# file.write("my first file.")
# file.close()

# file = open("file","r")
# print(file.read())
# file.close()

# file = open("file","a")
# file.write("\n this is a appended line.")
# file.close()

# file = open("file","r")
# print(file.read())
# file.close()

# file = open("file","r")
# print(file.readline())
# file.close()

# file = open("file","r")
# print(file.readline(15))
# file.close()

# file = open("file","r")
# for i in file:
#     print(i)
# file.close()
