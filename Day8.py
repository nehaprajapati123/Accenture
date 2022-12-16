
####Polymorphism: method overloading :- a method work different for every different circumstances.
#        
#x = 5
#
#x = 6
#
#print(x)    
#def tv(channel_number):
#    print("channel changed")
#    
#def tv():
#    print("channel not changed")
#    
#tv()

# class Person:
#    def Hello(self,name=None):
#        if name is not None:
#            print("Hello "+name)
#        else:
#            print("Hello")
# obj1 = Person()
# obj1.Hello("msk")

#
#class compute:
#    def area(self,x=None,y=None):
#        if x!=None and y!=None:
#            return x*y
#        elif x!=None:
#            return x**2
#
#        else:
#            return 0
#            
#c1 = compute()
#
#print(c1.area())
#print(c1.area(4))
#print(c1.area(4,5))

# def add(a,b):
#    if type(a) == int and type(b) == int:
#        print(a+b)
#    elif type(a)==str and type(b)==str:
#        print(a,"",b)
   
# add('4','5')


######method overriding -- child class method will have power to overload the parent class method: 


# class Animal:#parent class
    
#         def feed(self):
#             print("I eat food")
# class Herbivorous(Animal):#child class
#     def feed(self):
#         print("I eat only plants, I am vegetarian")
    
# rabbit = Herbivorous()
# rabbit.breathe()
# rabbit.feed()
# rabbit.run()

# que1:-Create a class called Mathematics. Define a add function. The function should work if u are giving 2 numbers or 3 number or n numbers , it should add and give the output. If no number is given it should return 0 as output.
# Hint: use arbitrary keyword argument for input.

# class Mathematics:
#     def add(self,*num):
#         print()
# result = Mathematics()   
# result.add(21,45)

# class Mathematics:
#     def add(self,*num):
#         sum = 0
#         for i in num:
#             sum = sum+i
#         print(sum)
# result = Mathematics()
# result.add(21,13)



#que2:-Create a class called area. Create a function which will calculate area of square if one input is given, if two inputs given calculate and print the area of rectange, if no input is given it should print “Nothing to find”

# class Area:
#     def area(self,*Paralen):
#         if len(Paralen)  == 1:
#             print(Paralen[0]*2,"sq/unit")
#         elif len(Paralen)  == 2:
#             print(Paralen[0]*Paralen[1],"sq/unit")
#         else:
#             print("Nothing to find")

# result = Area()
# result.area(2,2)


#que3:- Create a parent class Robot. Then a class that inherits from the class Robot. We add a method action that we override: . Create a method named action in both parent and child class. Create a object for child class and call the action method.

# class Robot:
#     def earn(self):
#         print("I earn")
#     def action(self):
#         print("ParentRobot")

# class ChildRobot:
#     def study(self):
#         print("I study")
#     def action(self):
#         print("ChildRobot")



# obj = ChildRobot()
# obj.action()

###########################################################################################
#datetime module:
# import datetime
# from enum import auto

# import numpy
#print current date and time
#default format of datetime:
#
# YYYY-MM-DD HH:MM:SS --- timestamp
#
#
#HH - 24 HOURS
#datetime.now()
# current_date_time = datetime.datetime.now()
# print(current_date_time)
##print(type(current_date_time))
#
#
# print(current_date_time.year)
# print(current_date_time.month)
# print(current_date_time.day)
# print(current_date_time.hour)
# print(current_date_time.minute)
# print(current_date_time.second)


#timedelta functions:convert from one time zone to another#####################

#IST - Indian Standard Time 
#UTC - 
#
#IST = UTC + 5.30
#PST = UTC - 7.00
# cur_time = datetime.datetime.now()
#print(cur_time)
#
#us_cur_time = cur_time + datetime.timedelta(hours=5 , minutes = 30)
#
#print(us_cur_time)
#
#silicon_valley_time = cur_time - datetime.timedelta(hours=7)
#print(silicon_valley_time)
#datetime.strftime() ---- string format function
#convert datetime objects to string data type 
#
#2020-01-22
#
#01,January 2022

#%a - weekday in short( eg: sun,mon,tue)
#%A - weekday in full(eg: Monday,Tuesday)
#%w - weekday as number(eg: 0 ,1,2,3,4,5,6.0 is sunday  )
#%d - day of the month( eg: 01 , 02 , to 31)
#%b - month in short form ( eg: jan,feb,mar)
#%B - month in full form ( eg: January)
#%m - month in number (eg: 01,02,...12)
#%y - year in short fomr ( eg: 22,23,24 last two digits)
#%Y - year in full form ( eg: 2022, 2023)
#%H - hour ( 24 hour clock)(eg: 00,01,23)
#%I - hour ( 12 hour clock)(eg: 01,02...12)
#%p - (AM,PM)
#%M - minute(00 ...59)
#%S - (second(00...59))
#%f - microsecond

#convert the current date and time into string. Also print
#date and time in eg: "November 27, 2020 08:20:03 PM"
#cur_time = datetime.datetime.now()
#
# print(cur_time.strftime("%B %d,  %H:%M:%S %p"))

#strptime -- convert str to timestamp
# time = "Sep 11,1993 08:22:13 AM"
#
#
# print(datetime.datetime.strptime(time,"%b %d,%Y %H:%M:%S %p"))
#last_solar_eclipse = "26-Dec-2019 03-34-00 AM"
#
#
#An eclipse will repeat itself in 6585 days:
# last_solar_eclipse_string = "26-Dec-2019 03-34-00 AM"
#print(type(last_solar_eclipse_string))
# last_solar_eclipse_timestamp = datetime.datetime.strptime(last_solar_eclipse_string,"%d-%b-%Y %H-%M-%S %p")
#print(type(last_solar_eclipse_timestamp))
# next_solar_eclipse = last_solar_eclipse_timestamp + datetime.timedelta(days = 6585)
#print(next_solar_eclipse)
# next_solar_eclipse_string = next_solar_eclipse.strftime("%B %d,%Y %H:%M:%S %p")
#print(next_solar_eclipse_string)

### we learn:-
#datetime.now()---current time of your system
#datetime.timedelta() --- used to add / subtract time
#strftime - convert timestamp to string
#strptime --- convert string to timestamp
#day
#year
#month
#date
#minute
#hour
#second
#date() and time()

#sweety_birthday = datetime.date(2002,1,3)
#
#print(type(sweety_birthday))
#
# exam_time = datetime.time(hour = 2,minute=30, second = 12)
# print(type(exam_time))
# print(exam_time)


# from dateutil import relativedelta
#calculate days between dates
# d1 = "2021/10/20"
# d2 = "2022/2/20"
#convert string to date object
#d1 = datetime.datetime.strptime(d1,"%Y/%m/%d")
#d2 = datetime.datetime.strptime(d2,"%Y/%m/%d")
#
#
#result = relativedelta.relativedelta(d2,d1)#difference between dates in months
#result = result.months + (result.years*12)
#print(result)
#
#result = d2 - d1
#print(result.month)
#
# cur_time = datetime.datetime.now()
#
# print("Day of the week is" , cur_time.weekday())
# import calendar
# yy = 2038
#display the calendar
#print(calendar.calendar(yy))
# print(calendar.isleap(2022))

#matplotlib.pyplot as plt ############################################################
# #
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# print(plt.style.available)

##lineplot
##bar plot
##scatter plot
##pie chart
##line plot
# plt.style.use("dark_background")
# x = [2,3,4,5,6]
# y = [44,55,66,22,11]
# plt.figure(figsize = (10,10))
# plt.title("A simple graph")
# plt.plot(x,y,color = "brown",linewidth = 5,marker = 'o',ms = 20,mfc = "blue") #ms = markersize
# plt.xlabel("Temperature")
# plt.ylabel("sensor")
# plt.grid(color = "yellow",linewidth = 2)
# plt.show()

# days = [1,2,3,4,5]       ### legent and lebel are mandatory with each other if doing labelling
# enfield = [50,40,70,80,20]
# honda = [80,20,20,50,60]
# yamaha = [70,20,60,40,60]
# ktm = [80,20,20,50,60]
# plt.figure(figsize = (10,10))
# #plt.plot(days,enfield,linewidth=2,color ="yellow",label="enfield")
# #plt.plot(days,honda,linewidth=2,color ="orange",label="honda")
# #plt.plot(days,yamaha,linewidth=2,color ="pink",label="yamaha")
# #plt.plot(days,ktm,linewidth=2,color ="white",label="ktm")
# plt.scatter(days,enfield,marker='*',s = 50)
# plt.title("bike details ")
# plt.xlabel("kms")
# plt.ylabel("Days")
# plt.legend()
# plt.show()

#Bar chart
# #
# year = [2022,2023,2019,2020]
# sales = [300,400,500,200]
# plt.figure(figsize=(10,10))
# plt.bar(x,y)
# plt.show()

# data = [23,45,56,78,213]
# data1 = [33,44,55,66,77]
# x = [1,2,3,4,5]
# l2 = ["blue","brown",'yellow',"red","orange"]
# l1 = ["apple","banana","cherry","dates","figs"]
# plt.figure(figsize=(10,10))
# plt.bar(x,data,color="blue",label="data1")
# plt.bar(x,data1,color="yellow",label="data2")
# plt.grid()
# plt.legend()
# plt.show()

#que23:- Write a program to display a bar graph for two departments in a company, where the employee ids is in the x-axis and their salaries in the y-axis
# import matplotlib.pyplot as plt
# import matplotlib
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2.9,7.6,3.5,4,5.6]
# plt.figure(figsize=(10,10))
# plt.title("employee details")
# plt.xlabel("employee id")
# plt.ylabel("salary/LPA")
# plt.bar(x,y)
# plt.show()

# import matplotlib
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2.9,7.6,3.5,4,5.6]
# plt.figure(figsize=(10,10))
# plt.xlabel('x')
# plt.ylabel('y')
# plt.bar(x,y)
# plt.show()

# que24:-
# Write a program to create a line graph to show the profits of a company for the years 2015, 2016, 2017, 2018, 2019
# x = [2015, 2016, 2017, 2018, 2019]
# y = [30,50,46,50,69.4]
# plt.figure(figsize = (10,10))
# plt.title("Growth Rate")
# plt.plot(x,y,color = "blue",linewidth = 6,marker = "*",ms = 20,mfc = "black")
# plt.xlabel("years")
# plt.ylabel("profit percent/year")
# plt.grid(color = "yellow",linewidth = 1)
# plt.show()

# que25:-Create a program to display a pie chart showing the percentage of employees in different departments of a company
# import matplotlib.pyplot as plt
# plt.style.use("ggplot")
# per = [30,20,10,5,35]
# department = ["dep1","dep2","dep3","dep5","dep5"]
# plt.pie(per,labels = department,shadow=True,autopct="%1.0f%%")
# plt.legend(loc = "best")
# plt.show()



# pie chart
# plt.style.use("ggplot")
# fruits = [23,44,55,66,80]
# l2 = [0,0.30,0,0.5,0]
# l1 = ["apple","banana","dates","plum","cherry"]
# plt.pie(fruits,labels=l1,explode=l2,shadow = True,autopct = "%1.0f%%")#explode= distance,autopct=autopercentage
# plt.legend(loc = "best") #location
# plt.show()


# que27:-Write a program to display the next consecutive 10 dates from the current date

# import datetime
# curr_date = datetime.datetime.now()
# for i in range(1,11):
#     consecutive_day=curr_date + datetime.timedelta(days = i)
#     consecutive_day_str  = consecutive_day.strftime("%B %d,%Y")
#     print(consecutive_day_str)

# que28:-Write a program to accept the date of birth of two persons and find out, who is the older of the two [Hint:Use the datetime module]
# from datetime import date
# persn1 = datetime.date(2003,8,25)
# persn2 = datetime.date(2005,9,22)
# age1 = (date.today() - persn1) // datetime.timedelta(days=365.2425)
# age2 = (date.today() - persn2) // datetime.timedelta(days=365.2425)
# if persn1<persn2:
#     print(persn1,", persn1 is older")
# else:
#     print(persn2,", persn2 is older")



# .1 Write a Python script to display the various Date Time formats:-  

# a) Current date and time
import datetime
from datetime import date, timedelta

# date_time = datetime.datetime.now()
datetime = datetime.datetime.now()
print(datetime)
# print(date_time.strftime("%B %d,  %H:%M:%S %p"))
# print(type(date_time))

# b) Current year
# year = date_time.year
# print(year)

# c) Month of year
# month = date_time.month
# print(month)

# d) Week number of the year
# week = date_time.strftime("%V")
# print(week)

# e) Weekday of the week
# week_day = date_time.strftime("%u")
# print(week_day)

# f) Day of year
# year_day = date_time.strftime("%j")
# print(year_day)

# g) Day of the month
# month_day = date_time.strftime("%d")
# print(month_day)

# h) Day of week
# week_day = date_time.strftime("%A")
# print(week_day)


# 2 :-Write a Python program to determine whether a given year is a leap year
# date_time = datetime.datetime.now()
# year = date_time.year
# if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#     print("leap year")
# else:
#     print("not a leap year")


# 3:-Write a Python program to convert a string to datetime.  Sample String : Jan 1 2014 2:43PM Expected Output : 2014-07-01 14:43:00
# date_time = "Sep 11,1993 08:22:13 AM"
# print(datetime.datetime.strptime(date_time,"%b %d,%Y %H:%M:%S %p"))  


#4:- Write a Python program to get the current time in Python
# cur_time = datetime.datetime.now()
# print(cur_time)


#5:- Write a Python program to subtract five days from current date
# cur_date = datetime.datetime.now()
# five_day = datetime.timedelta(days = 5)
# print(cur_date-five_day)

#6:- Write a Python program to print yesterday, today, tomorrow.
# cur_date = datetime.datetime.now() 
# today =int( cur_date.strftime("%d"))
# yesterday = today - 1
# tomorrow = today + 1
# print(yesterday,today,tomorrow)

# 7.Write a Python program to add 5 seconds with the current time
# time = datetime.datetime.now()
# sec = datetime.timedelta(0,5)
# print(time+sec)


# 8.Write a Python program to add year(s) with a given date and display the new date.
# date = input("enter a date eg:25/08/2003\t")
# value = datetime.datetime.strptime(date,"%d/%m/%Y")
# year=int(value.year)
# add_year = int(input("how many years to add\t"))
# print(year + add_year)


# # 9.Write a Python program to get days between two dates. Sample Dates : 2000,2,28, 2001,2,28
# day1 = input("enter day1 eg:25/08/2003\t")
# day2 = input("enter day2 eg:25/08/2003\t")
# value1 = datetime.datetime.strptime(day1,"%d/%m/%Y")
# value2 = datetime.datetime.strptime(day2,"%d/%m/%Y")
# date1 = int(value1.day)
# date2 = int(value2.day)
# for i in range(date1,date2):
#     print(i)


# # 10.Write a Python program to add a month with a specified date.
# month =  int(input("enter month in digits\t"))
# date = "25/"+str(month)+"/2022"
# specified_date = datetime.datetime.strptime(date,"%d/%m/%Y")
# print(specified_date)


# a = "hello neha"
# print(list(a))
# print(a.split())

# class Name():
#     def x(self):
#         print(6)
# p1 = Name()
# print(Name)  #printing class
# print(p1)  # printing object
# p1.x()

# exeptional handeling:-
# a = 7
# try:
#     print(b)
# except:
#     print(None)

# numpy:-
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import datetime
# from datetime import date, delta


print(reversed('neha'))