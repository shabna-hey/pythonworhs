#functions
# build in code:  print(),len(),input(),append(),add()
from fourth import n2


#definition:
#a block of statement used to perform an operatio/task
#syntax
#def function name(parameters)
              # "function docstring"              #function definition
              #function body
              #return [expression]

#function name(argument) ------>    #function call

#define to find the sum of 2 numbers
# def add():
#     n1=int(input("enter the number"))
#     n2=int(input("enter the number"))
#     s=n1+n2
#     print("sum",s)
#     return
#
#
# add()


#0r

# def add(n1,n2):
#     s=n1+n2
#     print("sum",s)
#
# add(23,45)




#define a function to display "hello your name"
# def hello():
#     name=input("enter you name")
#     print("hello",name)
#     return
# hello()

#define a function the count of a specific character in a string
# def count_ch(s,ch):
#     count=0
#     for i in s:
#         if i==ch:
#             count=count+1
#     return count
# s=input("enter string")
# ch=input("enter the character")
# a=count_ch(s,ch)
# print(a)




#define a function to find the factorial of number
# def fact():
#     n=int(input("enter no"))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#         print("factorial",f)
# fact()

#define a function to check whether a number is amstrong or not
# def check_amstrong():
#     n = int(input("enter the number"))
#     s=str(n)
#     sum=0
#     l=len(s)
#     for i in s:
#         sum=sum+int(i)**l
#     if sum==n:
#        print("amstong")
#     else:
#        print("not amstrong")
# check_amstrong()

#define a function to check whether a number is prime or not
# def check_prime():
#     n=int(input("enter the number"))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#
# check_prime()



#define a function to find factors of a number

# def fact():
#     n=int(input("enter the number"))
#     for i in range(1, n + 1):
#         if n % i == 0:
#             print(i)
#     return
# fact()



#define a fuction that takes 3 argument and find the simple
#simple intrest=(principal_amount*year*rate)/100
# def interest(a,y,r):
#     s = (a* y* r) / 100
#     print("interest",s)
# a=int(input("enter amount"))
# y=int(input("enter year"))
# r=int(input("enter rate"))
# interest(a,y,r)


#define a function that takes string and a charcter as arguments and tprint the count of charcter in the string
# def count_character(string,character):
#     count=0
#     for i in string:
#         if i==character:
#             count+=1
#     print(count)
#     return
# string=input("enter string")
# character=input("enter character")
# count_character(string,character)

# def add(n1,n2):
#     s=n1+n2
#
#     return s
# a=add(23,45)

#define a function that takes 3 numbers and return the product as result call the function and print the result

# def product(n1,n2,n3):
#     p=n1*n2*n3
#     return p
# n1=int(input("enter number"))
# n2=int(input("enter number"))
# n3=int(input("enter number"))
# pro=product(n1,n2,n3)
# print(pro)

#


