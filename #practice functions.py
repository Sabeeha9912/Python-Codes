#practice functions
# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# function call and store values in parameters
# cal_sum(5,10)
# For other
# cal_sum(10,14) 
# To find average
# def find_average(a,b,c):
#     average=(a+b+c)/3
#     print(average)
#     return average
# function call
# find_average(2,4,6)
# find_average(6,7,8)
# lenth of list
# cities=["islamabad","lahore","karachi"]
# colleges=["pgc","aspire","royal"]
# def list_len(list):
#     print(len(list))
# list_len(cities)
# list_len(colleges)
# factorial
# def find_fact(a):
#     f=1
#     for i in range (1,a+1):
#      f=f*i
#     print(f)
# find_fact(6)
#convert dollar to rupee
# def calc_rup(a):
#     b=200*a
#     print(b)
#     return(b)
# calc_rup(300)
#Greater no.
# def find_grt(a,b,c):
#     if a>b and b>c:
#         print("Greater no. is:",a)
#     elif b>a and a>c:
#         print("Greater no. is:",b) 
#     else:
#         print("Greater no. is:",c) 
# find_grt(3,6,7)    
# find_grt(4,6,8)
#For table
# def fin_table(a):
#     a=int(input("Enter any no:"))
#     i=1
#     while i<=10:
#         print(a*i)
#         i=i+1
# fin_table(5)                             
#for quardrant
# import math
# def get_quardrant(x,y):
#     if  x>0 and y>0:
#         return "1st quardrant"
#     elif x<0 and y>0:
#         return "2nd quardrant"
#     elif x<0 and y<0:
#         return "3rd quardrant"
#     elif x<0 and y<0:
#         return "4th quardrant"
#     else:
#         return "At origin"
# #To take input
# x1,y1=map(int,input("Enter the points(x1,y1):").split(','))
# print(get_quardrant(x1,y1))
# x2,y2=map(int,input("Enter the points(y1,y2): ").split(','))
# print(get_quardrant(x2,y2))
# distance=math.sqrt ((x2-x1)**2+(y2-y1)**2)
# print("distance is:",distance)
# SUM:
# num1=int(input("Enter 1st Number "))
# num2=int(input("Enter 2nd Number "))
# large=max(num1,num2)
# print(f"{large} is greater between {num1} and {num2}")
# Factorial functions
# find_fact(9) # just call function to test.
#To  find sum of 2 no.
# def add_numbers(a,b):
#     sum=a+b
#     print("Sum is:",sum)
# add_numbers(4,7)
# print(add_numbers.__doc__)
#lab...1:
# def greet(name= "guest"):
#    print("Hello", name)
# greet("sabeeha")
# greet() #without arguments it will return default arguments like guest.
#2:
# def add(a,b):
#     print(a+b)
# add(3,2) # no. of aruguments must pass = parantheses.
# add(5,7,9) # it will create error
#3:
# def intro(name,age,sec):
#     print(f"my name is {name} and age is {age} and sec is {sec}")
# intro(age=19,name="Sabeeha", sec="B") # i have changed order that has no effect.
# 4:
# def info(**data):
#     print(data)
# info(name="Sabeeha" , age=19 , sec="B") # ** conver it in disc. so we pass key:value.
#5:
# avg=lambda x,y,z:(x+y+z)/3
# def square(a=avg(3,4,5)):
#     return a*a
# print(square())
List = [1, 2, 3, 4]
for i in List:
    if i == 2 or i == 3:
        List.remove(i)
print(List)







