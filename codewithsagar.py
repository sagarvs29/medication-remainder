# print("hi how are you \nI am fine")
# calculator................................................................................
# print("calculator")
# a=int(input(" enter a"))
# b=int(input(" enter b"))
# op=input(" enter the operator")
# if op=='+':
#     print(" addition of a and b")
#     res=a+b
#     print(res)
# elif op=='-':
#     print(" substraction")
#     res=a+b
#     print(res)
# elif op=='*':
#     print(" multiplication")
#     res=a*b
#     print(res)
# elif op=='/':
#     print(" division")
#     res=a/b
#     print(res)
# elif op=='%':
#     print(" modulus")
#     res=a%b
#     print(res)
# elif op=='-':
#     print(" substraction")
#     res=a+b
#     print(res)
# elif op=='**':
#     print(" power")
#     res=a**b
#     print(res)
# str="15"
# a=15
# strnum=int(str)+a
# print(strnum)
# for character in str:
#     print(character)
# hlo=" hi all okay how are you"
# print(hlo[-6:-2])
# operations in string................................................................
# a="hi iam sagar"
# #length
# print(len(a))
# #slicing
# print(a[0:5])
# print(a[-8:-2])
# methods in strings.........................................................................
# a="hey after graduation life is hell 123"
# # upper
# print(a.upper())
# # lower
# print(a.lower())
# #rstrip ( remove the symols in a word)
# print(a.rstrip("!"))
# #replace
# print(a.replace("Hey after graduation life is hell!!!!!!!!123","dont know man123"))
# #capitilize
# print(a.capitalize())
# # centre (for how much gap we need)
# print(a.center(150))
# #count
# print(a.count("is"))
# #endswith
# print(a.endswith("z"))
# #find
# print(a.find("er"))
# #index
# print(a.index("u"))
# #isalnum(to check atoz,ATOZ,0to9)
# b="hlohi123"
# print(b.isalnum())
# #isalpha
# c="Hlooman"
# print(c.isalpha())
# #isspace
# d=" "
# print(d.isspace())
# #istitle (if a word start with  capital letter true else false)
# print(a.istitle())
# print(c.istitle())
# #startswith
# print(a.startswith("h"))
# #swapcase
# print(a.swapcase())
#conditional statements....................................................................................................
#if else
# age=int(input(" enter the age"))
# if(age>=18):
#     print("your eligible for marriage")
# else:
#     print(" your still minor")
#if elif else
# city=input(" enter the city u wish to visit\n")
# if city=="mysuru":
#     print("25000 is the total cost for mysuru package ")
# elif city=="shivmogga":
#     print("10000 is the total cost for shivmogga package")
# elif city=="udupi":
#     print(" the total package for udupi is 50000 ")
# else:
#     print(" your place is not in our list")
import time
timestamp=time.strftime()
print(timestamp)