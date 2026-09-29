# # # Q1.Define a function that takes 2 numbers and returns their product
#
# def product(a,b):
#     p=a*b
#     return p
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# pro=product(a,b)
# print(pro)
# # Q2.Define a function that takes a string and returns number of vowels
#
# def string_vowel(s):
#     count=0
#      for i in s:
#          if i in "aeiouAEIOU":
#             count=count+1
#     return count
# s=input("enter the string")
# n=string_vowel(s)
# print("number",n)
# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle

# def area(l,b):
#     a=l*b
#     return a
# l=int(input("enter the lenght"))
# b=int(input("enter the bearth"))
# rect=area(l,b)
# print(rect)
#
# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]
# def even(l):
#     new_list=[]
#     for i in l:
#         if i%2==0:
#             new_list.append(i)
#     return new_list
#
# a=even(l)
# print("even number",a)



# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# def sum_of_digits(l):
#     result = []
#     for i in l:
#         total = i // 100 + (i// 10) % 10 + i% 10
#         result.append(total)
#     return result
#
# a=sum_of_digits(l)
# print(a)
#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]
# def common_elements(l):
#     result = []
#     for i in l:
#         if i not in result:
#             result.append(i)
#     return result
#
# a=common_elements(l)
# print(a)

#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# def common_elements(list1, list2):
#     result = []
#     for i in list1:
#         if i in list2:
#             result.append(i)
#     return result
#
# a = common_elements(list1, list2)
# print(a)


#define a function that takes string as arguments and return a new dictionary where the function and print the dictionary

# s="python coding is easy and fun"
# def create_dict(s):
#     new={}
#     words = s.split()
#     for i in words:
#         new[i]=len(i)
#     return new
#
# a= create_dict(s)
# print(a)


####types of arguments

#positional arguments


# def name(n,a):
#     print("name",n)
#     print("Age",a)
#     return
# name("arun",23)



#keyword arguments

# def name(n,a):
#     print("name",n)
#     print("Age",a)
#     return
# name(n="arun",a=23)
#name(a=23,n="arun")


#default arguments
# def fun(n,a=23):
#     print("name",n)
#     print("age",a)
#     return
# fun('arun',24)
#variable length arguments
# two types
#arbitary positional arguments
# def fun(*args):
#     print(args)
#     return
# fun(10,20)
# fun(10,20,30)
#arbitary keyword arguments
# def fun(**kwargs):
#     print(kwargs)
#     return
# fun(a=10,b=20,c=40)
# fun(a=10,b=20,c=30,d=50)


#difne a function to find the sum of number using arbitary positinal arguments

# def add(*args):
#     s = 0
#     for i in args:
#         s = s + i
#     return s
#
# a=add(10, 20, 30)
# print(a)


#largest 3 number
# def large(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>a:
#         return b
#     else:
#         return c
#
# a=int(input("enter the 1 no"))
#
# b=int(input("enter the 2 no"))
# c=int(input("enter 3 no"))
# d=large(a,b,c)
# print(d)



