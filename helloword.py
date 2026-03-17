print("hello world", end=" ")
print("welcome python")
print("laptop","mouse","keyboard",sep="\'")


# escape sequence

# \n
# \t


# jgjgvghfghfhg - single line comment

'''
print("hello")
print("welcome")
print("hi")

multiline command
'''

# data Types

'''
simple dataType

1. integer  - 100

2. string   - "whatever"

3. float    - 50.2

4. boolean  - True , False

'''

'''
complex DataType

1. list

2. Dictionary

3. Tuple

4. set

'''

# variables 

name = "navi"
age = 15

print(name,age , sep=",")

# assignment 

# single assignment

n = 5

print("sigle assignment :- ", n)

# multi assignment

name1,age1,launguage = "navi",15,True

print("multi assignment :- ", name1, age1,launguage)



# Indexing

name2 = "john"

print(name2[0])

# immutability

# name2[0] = "R"

# print(name2)



# operators


'''
1 . arithmetic operator
2 . assignment operator
3 . comparision operator
4 . logical operator
5 . bitwise operator
6 . membership operator
'''

# 1. arithmetic operator 

# addition      +

print(1 + 3)

# subraction    -

print(2 - 1)

# multiplication *

print(3*3)

# division   /

print(5 / 5)

# modulus    %

print(9%10)

# Exponencial **

print(4**2) # 4^2 = 4*4 = 16


# floar division // 

print(10 // 2)

'''
Bodmas 

b - bracket
o - order
d - diviaion
m - multiplication
a - addition
s - subraction
'''



print(2**3**(2%10)) #        2**3**2 = 2^9

print(2**9)



# Assignment operator

num1 = 10
additionVal = 100

num1 /=  additionVal

print(num1)


# comparision & Relational operator

'''
lessThen     <       (5<5)     False

greaterThen  >       (5>5)     False

lessThenEq   <=      (5<=5)    True

GreaterThenEq >=     (10>=2)   True

   ==     (10=="10") False

   !=     (10 != "10") True



'''
print(10>10)
print(10>.5)
print(10=="10")

print("10")
print(10)


a = "siva"
b = "Siva"

print("s :-", ord("s"))
print("S :-", ord("S"))

print(a==b)



a = 5
b = 7

print(a,b)

# temp = a

# a = b 

# b = temp

# print(a,b)

a,b = b,a

print(a,b)



# membership operator [in] , [not in]

group = [1,2,3,4,5]

print(50 not in group)


# logical operator

'''
AND   -- > and
OR    -- > or
NOT   -- > not

'''


# AND 

# True and True and True = True 
# True and False and True = False


# OR

# True or False or False = True
# False or False or False = False

# NOT

# not(True) = False
# not(False) = True 


print(5>5 and 5==5 and 1>=.1000) # False
print(5==5 or 5>=3 and 2==2) # True
print(not(6>=2) and 8>3) #False


# Bitwise operator 

'''
AND  - &
OR   - |
NOT  - ~
XOR  - ^
leftShift - <<
RightShift - >>
'''

'''
XOR - ^


T   T    - F
T   F    - T
F   T    - T
F   F    - F
'''


a = 5

b = 7


print(a & b)
print(a | b)
print(~b)
print(a ^ b)


print(12 << 1) 
print(12 >> 1)



# String - "Adsf"

# string Replication 


a = "hello"

print(a * 5)

# string concatination  +

str1 = "iron"
str2 = "man"
str3 = " "

print(str1 +str3 + str2)


# user Input Console    (input())

# name = input("enter your name : - ")

# print("userName :- ",type(name))


# age = input("enter your age :- ")
# print("userAge :- ",type(age))


# TypeCasting 


# num2 = int(input("enter your mark Maths :- "))
# num3 = int(input("enter your mark Science :- "))

# print((num2+num2)/2)


# a = int(input("enter first value :- ")) #3
# b = int(input("second first value :- ")) #2

# print(3*a*2+b - 2) #error #18


#unit digit


# num = input() #10000 , 0 - 1, 1 - 0 , 2 - 0 , 3 - 0 ,4 - 0
# print(num[len(num)-1]) # num[len(num)-2]

# print(1234//10) --> 123


# num1 = int(input())

# num1 //= 10 #num1 = num1 // 10 = 1234 // 10 -- > 123

# print(num1 % 10) #123 % 10 --> 3


# flow control Statement

# # 1. conditional statement

# # 1. if statement

# # if condition = true --> next line , false --> if inside not allow

# # example 

# if (5>=5) :
#     print("now i think condition true")


# # 2.if else statement

# # if (5>5) :
# #     print("condition true")
# # else :
# #     print("condition false")


# # # 3. Elif Statement

# # time = int(input("enter the time Now :- 24hrs"))

# # if (time >= 1 and time <= 6) : 
# #     print("good morning")
# # elif (time >= 7 and time <=12) :
# #     print("morning")
# # elif (time >= 13 and time <= 17) : 
# #     print("Good Afternoon")
# # elif (time >= 18 and time <= 20) :
# #     print("Good Evening")
# # else :
# #     print("Good night")


# # #4. Nested If Statement 


# # # uniform entrance selection application
# # name = input("enter your name")
# # age = int(input("enter your age"))
# # height = int(input("enter you height using cm"))
# # weight = int(input("enter your weight using kg"))

# # if (age >= 18) :
# #     if (height >= 160) : 
# #         if (weight >= 60) :
# #             print(name ," congradulation your selected 😊😊😊")
# #         else : 
# #             print(name, " your weight is not eligible")

# #     else : 
# #         print(name, "  your height is not eligible")
# # else : 
# #     print(name, " your age is not eligible")


# # 5. match statement


# # match variable :
# #     case value : statement


# # example 


# day = int(input("enter the today number :- "))


# match day :
#     case 1 :
#         print("sunday")
#     case 2 :
#         print("monday")
#     case 3 :
#         print("tuesday")
#     case 4 :
#         print("wednesday")
#     case 5 :
#         print("thursay")
#     case 6 :
#         print("friday")
#     case 7 :
#         print("saturday")
    













