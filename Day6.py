##OOPS ##############################constuctors and inheritance
#
##Object Oriented Programming ----design methodology
##
##
###features of oops concept:
##
##resuability of code
##DRY --- Dont repeat yourself 
#
# import random
##print(type(5))
##print(type(5.5567))
##print(type("msk"))
##print(type([1,2,3]))
##print(type((1,2,3)))
# print(type(random))
# print(type(range))
#
#
#class and object:
#
#class --- template / blueprint: house A
#    
#object ----cloned class . house B
#class has two things --- property(features) and attribute(behaviour / action)
#
# class Dog:
#     num_of_legs = 4 #class variable
#     num_of_teeth = 42
#     have_beak = False
#     can_fly = False
#     can_swim = True

#     def bark(self):
#         print("bow bow")
# #    
# #    
# print(Dog.num_of_legs)
#
#
#Object / Instance
# husky = Dog() # object creation
# happy = Dog() # object creation
# golden_retriver = Dog()
# beagle = Dog()
# a = Dog()
# print(husky.num_of_legs)
# print(happy.num_of_legs)
# golden_retriver.bark()
# print(golden_retriver.can_fly)
# #class Method / Functions:

# class:-
# class Girl:
#     name = "neha" #class variable

    # method/fun:-
#     def laugh(self): #self is mandaroty/ instance attribute
#         print("haha")

# print(Girl.name) 

# # object:-
# female = Girl()
# print(female.name)

# Girl.laugh(None)  
# female.laugh()

#constructor ----- inbuilt function
#__init__()----initialize the instance variable/ object variable
#constructor never return anything
#only one constructor in one class

#self ---- pointer to the current object of the class

# class:-
# class Family:
#     family_name = "Parr" # class variable
#     def __init__(self,fname,lname,age,gender):#instance variables
#         self.fname = fname # initialise the instance variable
#         self.lname = lname
#         self.age = age
#         self.gender = gender

#     # method:-
#     def full_name(self):
#         print(self.fname + " " + self.lname)

# # object:-
# father  = Family("bob","Parr",44,"male")
# mother = Family("lily","parr",38,"female")
# # print(father.age,father.fname,mother.gender,mother.lname)
# father.full_name()
# mother.full_name()
# print(father.family_name)


# class Girl:
#     def __init__(self,name,lname,age,height):
#         self.name = name
#         self.lname = lname
       
#     def fullname(self):
#         print(self.name,self.lname)
# info = Girl("neha","nsp")
# info.fullname()

# class Vehicle:
#     Vehicle = "bike"
#     def __init__(self,max_speed,mileage):
#         self.mileage = mileage
#         self.max_speed = max_speed
#     def bike_details(self):
#         print(self.max_speed, self.mileage)
# info = Vehicle("300km/hr","xyz")
# info.bike_details()

# class Students:
#     school_name = "JNV"
#     def __init__(self,name,age, Class):
#         self.name = name
#         self.age = age
#         self.Class = Class
#     def school_details(self):
#         print(self.name,self.age,self.Class)
# info = Students("neha","12th",17)
# info.school_details()

# class Student:
#     def __init__(self,name,age,contact):
#         self.name = name
#         self.age = age
#         self.contact = contact
#     def fun(self):
#         print(self.name,self.age,self.contact)
# obj = Student('neha', 19, 7678558027)
# obj.fun()


##features of oops 
#
##inheritance
##encapsulation
##polymorphism
#
#
##inheritance: --- used to share the properties of the class with another class.
#
##single
##multiple
##multilevel
#
#
# class Person: #base class/ Parent class
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# class Teacher(Person):#child class / derived class
#     def __init__(self,name,age,gender,grade,subjects=None):
#         Person.__init__(self,name,age,gender)#inheriting
#         self.grade = grade
#         self.subjects = []
#     def add_subjects(self,new_subject):
#         if new_subject not in self.subjects:
#             self.subjects.append(new_subject)
#         else:
#             print("The subejct already exists")
#     def remove_subjects(self,old_subject):
#         if old_subject in self.subjects:
#             self.subjects.remove(old_subject)
#         else:
#             print("Subject doenst exists")
# t1 = Teacher("lily",33,"female",10)
# t1.add_subjects("maths")
# t1.add_subjects("english")  

# print(t1.name,t1.age,t1.gender,t1.subjects)

# class Student(Person):
#     def __init__(self,name,age,gender,school_name,fees):
#         Person.__init__(self,name,age,gender)
#         self.school_name = school_name
#         self.fees = fees
#     def increase_fee(self):
#         self.fees *= 1.5
#         print(self.fees)
# s1 = Student("viv",12,"male","ABC",10000)
# print(s1.name,s1.age,s1.gender,s1.school_name,s1.fees)
# s1.increase_fee()
# class Alumni(Student):
#     def __init__(self,name,age,gender,school_name,fees,grad_year):
#         Student.__init__(self,name,age,gender,school_name,fees)
#         self.grad_year = grad_year
# a1 = Alumni("msk",22,"female","ABC",10000,2022)
# print(a1.name,a1.age,a1.gender,a1.fees)


# class Vehicle:
#     def __init__(self,type,milage,model):
#         self.type = type
#         self.milage = milage
#         self.model = model
# class Bus(Vehicle):
#     def __init__(self,type,milage,model,color):
#         Vehicle.__init__(self,type,milage,model)
#         self.color = color
# info_Bus = Bus("Bus","100km/hr","xyz","white")
# print(info_Bus.type,info_Bus.milage,info_Bus.model,info_Bus.color)



# class Child:
#     def __init__(self,capacity,build_year):
#         self.capacity = capacity
#         self.build_year = build_year
# Child_obj = Child("abc",2022)
# print(Child_obj.capacity)
# print(Child_obj.build_year)


# class Grandparent():
#     def __init__(self,eyeColor):
#         self.eyeColor = eyeColor
# class Parent():
#     def __init__(self,eyeColor,hairColor): 
#         Grandparent.__init__(self,eyeColor)
#         self.eyeColor =eyeColor
#         self.hairColor = hairColor
# class Son():
#     def __init__(self,eyeColor,hairColor,skinColor):
#         Parent.__init__(self,eyeColor,hairColor)
#         self.eyeColor = eyeColor
#         self.hairColor = hairColor
#         self.skinColor = skinColor

# Grandparent_info = Grandparent("green")
# print(Grandparent_info.eyeColor)

# parent_info = Parent("grey","yello")
# print(parent_info.eyeColor,parent_info.hairColor)

# son_info = Son("hazel","grown","fair")
# print(son_info.eyeColor,son_info.hairColor,son_info.skinColor)



    










# exer1:-
# def fun1(name, age):
#     print(name, age)
# fun1("neha",19)

# exer2:-
# def name(*name):
#     for i in name:
#         print(i)
# name("neha","mmy","papa","bro")

# exer3:-
# def calculation(num1,num2):
#     addition = num1+num2
#     subtraction = num1-num2
#     return addition,subtraction  
# print(calculation(2,4))

# exer4:-
# def showEmployee(name,salary = 9000):
#     print(name,":",salary)
    
# showEmployee("haary potter")
# showEmployee("neha",10000)



# exer5:-
# def fun1(a,b):
#     def fun2(a,b):
#         addition = a+b
#         return addition
#     print(fun2(a,b)+5)
    
# fun1(3,4)


# que6:-
# def sum(n):
#     if n <= 1:
#         return n
#     else:
#         return n + sum(n-1)
    
# print(sum(10))


# exer7:-(1)
# def fun1():
#     return ("important info")
# info = fun1()
# print(info)
# # (2):-
# def fun1():
#     return ("important info")
# def fun2():
#     return fun1()
# print(fun2())


