# #1Given a string
# s="I am learning Python"
#
# # find the length of the string
# print("the length of:", len(s))
#
# # find the reverse of the string
# print("the reverse of:",s[::-1])
#
# # find the last character of the strings
# print("last character",s[-1])
# #find the 13th character
# print("13th character",s[12])
# #print the characters from 2nd index to 15 th index
# print("2nd to 15th ",s[2:15])
#
# #combines the string s with word "programming"
#
# print(s + ' programming')
# #2.Given a list
# l=['Guitar','Piano','Violin','Drums','Flute']
# # Add a new item 'Veena' to the list
# l.append("veena")
# print(l)

# #3Declare a list of 5 food items
# l=['biriyani','loaded fries','idili','rice','dosa']
#
# #     #Add new fooditem to the list
# #
# l.append("noodles")
# print(l)
# #     #change the second food item
# l[1]='mandi'
# print(l)
#
# #     #print the updated list
# l[3]='loaded fries'
# print(l)
# #     #print the last food item
# print('last food ',l[-1])
# #     #print the number of food items
# print("the item is:",len(l))
# #4.Given a string
# s="python is a programming language"
#
# # #Remove the first 10 characters and print the remaining
# print("10 chacater",s[10:32])
# # #print the last 5 characters
# print(s[-5:])

# l=[10,56,23,67,19,70]
#
# #interchange 2nd index and 5th index numbers
# l[1],l[4] = l[4],l[1]
# print(l)
# #6iven a set
# s={10,20,30,40}
# # Add a new number 50 to the set
# s.add(50)
# print(s)

#1
# l=[10,20,30,40,50,60]
# print('numbers',l[1:5])
# #2
# l[0],l[5] = l[5],l[0]
# print(l)
#3
# s="python programming"
# if "python" in s:
#     print("yes")
# else:
#     print("no")

# #4
# l=[10,20,10,30,20,40]
# print(l.count(10))
#
# l=[45,12,67,23,89,10]
# largest=0
# for i in l:
#     if i>largest:
#         largest=i
# print(largest)


#6

# l=[10,20,30,40,50]
# # print("reverse",l[::-1])
#
# #with revese
#
#
# l.reverse()
# print(l)
# s="python"
# for i in s:
#     print(i)



#
# l=[10,20,30,40]
#
# s=0
# for i in l:
#     s+=i
# print(s)



s = "I am learning Python"
# Find the length of the string.
# print("length",len(s))
# Find the reverse of the string.
# print("reverse:",s[::-1])
# Find the first character.
# print(s[0])
# Find the last character.
# print(s[-1])
# Find the 5th character.
# print(s[5])
# Find the 10th character.
# print(s[11])
# Print characters from 3rd index to 12th index.
# print(s[2:13])
# Print the first 5 characters.
# print(s[:6])
# Print the last 6 characters.

# Combine the string with "programming".
# print(s+"programming")

# # Write a program to read two numbers and find their sum.
# n1=int(input("enter the number"))
# n2=int(input("enter the number"))
# print(n1+n2)

# Write a program to find the area of a circle.

# n=int(input("enter the area"))
# area=3.14*n*n
# print("area of the circle",area)
# # Write a program to convert Celsius to Fahrenheit.
# c = float(input("Enter Celsius: "))
# f = (c * 9/5) + 32
# print("Fahrenheit =", f)
# Write a program to swap two numbers.
# a=20
# b=40
# temp=a
# a=b
# b=temp
# print("After swapping:")
# print("a =", a)
# print("b =", b)

# Write a program to find the largest of two numbers.
# a=int(input("enter the no"))
# b=int(input("enter the no"))
# if a>b:
#     print("largest no1",a)
# else:
#     print("largest no1",b)

# Write a program to check whether a number is even or odd.
# n=int(input("enter the number"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")


#list using for loop
# l=[2,3,45,6,7,9]
# new=[]
# for i in l:
#     if i%2==0:
#
#         new.append(i)
# print(new)

#
# # Write a program to check whether a number is positive, negative, or zero.
# n=int(input("enter the number"))
#
# if n>0:
#     print("positive",n)
# elif n<0:
#     print("negative",n)
# else:
#     print("zero",)

# # Write a program to find the largest of three numbers.
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)


# Write a program to check whether a person is eligible to vote.
# p=int(input("how old are you"))
# if p>=18:
#     print("eligible")
# else:
#     print("not eligible")



# Write a program to check whether a given year is a leap year
# n=int(input("enter the number"))
# if n%400==0:
#     print("leap year")
# elif n%100==0:
#     print("not leap year")
# elif n%4==0:
#     print("leap year ")
# else:
#     print("not leap year")

# l=[1,2,0,4,0,6,7]
# new=[]
# for i in l:
#     if i!=0:
#         new.append(i)
# for i in l:
#     if i==0:
#         new.append(i)
# print(new)




# divisible by 400
#divisible by 4 and 100!=0



#fuction
#define to find the sum of 2 numbers
# def add():
#     n1=int(input("enter the number"))
#     n2=int(input("enter  the number"))
#     s=n1+n2
#     return s
# a=add()
# print(a)

# Define a function to find the difference of two numbers.
# def difference():
#     n1=int(input("enter the number"))
#     n2=int(input("enter the number"))
#     d=n1-n2
#     return d
# a=difference()
# print("difference is:",a)



# Define a function to find the product of two numbers.
# def product():
#     n1=int(input("enter the no"))
#     n2=int(input("enter the no"))
#     p=n1*n2
#     return p
# a=product()
# print(a)

#

#
# Define a function to check whether a number is even or odd.
# def even_odd():
#     n=int(input("enter the number"))
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# a=even_odd()
# print(a)
#
# Define a function to find the square of a number.
# def square():
#     n=int(input("enter the number"))
#     s=n*n
#     return s
# a=square()
# print(a)
#
# # Define a function to find the cube of a number.
# def cube():
#     n=int(input("enter the no"))
#     c=n**3
#     return c
# a=cube()
# print(a)
#
# Define a function to find the largest of two numbers.
# def largest():
#     a=int(input("enter the number"))
#     b=int(input("enter the number"))
#     if a>b:
#         return a
#     else:
#         return b
# n=largest()
# print(n)
# # Define a function to check whether a number is positive, negative, or zero.
# def number():
#     n=int(input("enter the number"))
#     if n>0:
#         return "positive"
#     elif n<0:
#         return "negative"
#     else:
#         return "zero"
# a=number()
# print(a)

#
# Define a function to find the area of a circle.
# def area():
#     l=int(input("entre the length"))
#     b=int(input("enter the breath"))
#     a=l*b
#     return a
# r=area()
# print(r)

# # Define a function to find the sum of all elements in a list.
# def add(l):
#     s=0
#     for i in l:
#         s+=i
#     return s
# l=[12,21,56,67,2]
#
# a=add(l)
# print(a)
#
# Define a function to count even numbers in a list.
# l=[2,3,4,5,6,7]
# def even(l):
#     c=0
#     for i in l:
#         if i%2==0:
#          c+=1
#     return c
# a=even(l)
# print(a)




#
# Define a function to count odd numbers in a list.
# l=[1,2,3,4,5,6,7]
# def odd(l):
#     c=0
#     for i in l:
#         if i%2!=0:
#             c+=1
#     return c
# a=odd(l)
# print(a)
#
# Define a function to return a new list containing only positive numbers.
# l=[2,-3,5,7,-1,-5]
# def positive(l):
#     new=[]
#     for i in l:
#         if i>0:
#             new.append(i)
#     return new
# a=positive(l)
# print(a)
#
# Define a function to remove duplicate elements from a list.
# l=[2,3,4,1,3,4,]
# def fun(l):
#     new=[]
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
# a=fun(l)
# print(a)

##amstrong####
# # Write a Python program using a function to check whether a given number is an Armstrong number or not.
# def armstrong(n):
#     c=0
#     s=str(n)
#     l=len(s)
#     for i in s:
#         c=c+int(i)**l
#     if c==n:
#         return "Armstrong"
#     else:
#         return "not armstrong"
#
# n=int(input("enter the number"))
# a=armstrong(n)
# print(a)
#
# def armstrong(n):
#     s = str(n)
#     l = len(s)
#     c = 0
#
#     for i in s:
#         c = c + int(i) ** l
#
#     if c == n:
#         return True
#     else:
#         return False
#
#
# for i in range(1, 1001):
#     if armstrong(i):
#         print(i)

# Print numbers from 1 to 100 using a for loop.
# for i in range(1,101):
#     print(i)
# Print numbers from 100 to 1.
# for i in range(100,0,-1):
#     print(i)
# Find the sum of numbers from 1 to n.
# n=int(input("enter the number"))
# s=0
# for i in range(1,n+1):
#     s=s+i
# print(s)


# # Find the factorial of a number.
# n=int(input("enter the number"))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)
# Print the multiplication table of a given number.
# n=int(input("enter the number"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)


# Count the number of digits in a number.
# n=int(input("enter the number"))
# c=0
# for i in str(n):
#     c=c+1
# print(c)

# Find the sum of digits of a number.
# n=int(input("entre the no"))
# sum=0
# for i in str(n):
#     sum=sum+int(i)
# print(sum)
# Reverse a number.

# n=int(input("enter the number"))
# rev=""
# for i in str(n):
#         rev=i+rev
# print(rev)


# Check whether a number is a palindrome.
# n=int(input("enter the string"))
# rev=""
# s=str(n)
# for i in str(n):
#     rev = i + rev
#
# if s==rev:
#     print("palindrome")
# else:
#     print("not palindrome")
# print(rev)

# Check whether a number is an Armstrong number.
# n=int(input("enter the number"))
# total=0
# s=str(n)
# l=len(s)
# for i in s:
#     total=total+int(i)**l
#
# if total==n:
#     print("armstong")
# else:
#     print("not armstrong")
# print(n)


# Find the Fibonacci series up to n terms.
# n=int(input("enter the no"))
# a=0
# b=1
# for i in range(n):
#     print(a,end="")
#     c=a+b
#     a=b
#     b=c

# Check whether a number is prime.
# def prime(n):
#     if n>2:
#         return "not prime"
#     for i in range(n,2):
#         if n%i==0:
#              return "not prime"
#     else:
#         return "prime"
#
# n=int(input("enter the number"))
# a=prime(n)
# print(a)





# Print all prime numbers between two given numbers.
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
#
# for n in range(start, end + 1):
#     count = 0
#
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count = count + 1
#     if count == 2:
#         print(n)


#Remove Duplicates
# l = [2, 3, 2, 5, 3, 7, 5]
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)

#Find Largest and Smallest
# l = [12, 45, 7, 23, 56, 9]
# large=l[0]
# small=l[0]
#
# for i in l:
#     if i>large:
#         large=i
#     if i<small:
#         small=i
# print("largest",large)
# print("smallest",small)

#4. Second Largest
# l = [10, 25, 8, 40, 15]
# large=l[0]
# second=l[0]
# for i in l:
#     if i>large:
#         second=large
#         large=i
#     if i>second:
#         second=i
# print("second last number",second)
#or
# print(l[-2])


#5. Even and Odd
# l = [1, 4, 7, 8, 10, 13, 16]
# even=[]
# odd=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print("even",even)
# print("odd",odd)


#positive or negative
# l = [2, -4, 6, -8, 10, -3]
# pos=[]
# neg=[]
# for i in l:
#     if i>0:
#         pos.append(i)
#     if i<0:
#         neg.append(i)
# print(pos)
# print(neg)

# 7. Sum of Elements
# Find the sum of all elements in a list without using sum().
# l=[1,2,3,4,5,6,7]
# total=0
# for i in l:
#     total=total+i
# print(total)

# 8. Count Even and Odd
# Count the number of even and odd elements in a list.
#
# l=[1,2,3,4,5,6,7,8,9]
# even=0
# odd=0
# for i in l:
#     if i%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print("count of even",even)
# print("count of odd",odd)


# 9. Reverse a List
# Reverse a list without using reverse() or slicing [::-1].
# l=[2,3,4,5,6]
# new=[]
# for i in range(len(l)-1,-1,-1):
#     new.append(l[i])
# print(new)

# l = [12, 45, 23, 67, 34, 89, 10]
# Find the largest number.
# largest=l[0]
# for i in l:
#     if i>largest:
#         largest=i
# print(largest)

# Find the smallest number.
# small=l[0]
# for i in l:
#     if i<small:
#         small=i
# print(small)
# Find the sum.
# total=0
# for i in l:
#     total=total+i
# print(total)

# Count even numbers.
# even=0
# for i in l:
#     if i%2==0:
#         even=even+1
# print(even)

# Count odd numbers.
# odd=0
# for i in l:
#     if i%2!=0:
#         odd=odd+1
# print(odd)


# Print the reverse.
# print(l[::-1])
# Find the length
# print(len(l))



# Write a user-defined function to find the sum of two numbers.

# def add(a,b):
#     sum=a+b
#     return sum
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# f=add(a,b)
# print(f)
#
# Write a function to check whether a number is even or odd.

# def even_odd(n):
#         if n%2==0:
#             return "even"
#         else:
#             return "odd"
# n=int(input("enter the number"))
# a=even_odd(n)
# print(a)
# Write a function to find the factorial of a number.
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# n=int(input("enter the number"))
# a=fact(n)
# print(a)
#
# Write a function to check whether a number is prime.
# def prim(n):
#     if n<2:
#         return "not prime"
#     for i in range(2,n):
#         if n%i==0:
#             return "not prime"
#
#     return "prime"
# n=int(input("enter the number"))
# a=prim(n)
# print(a)



# Write a function to find the largest number in a list.
# l=[2,3,45,80]
# def large(l):
#     largest=0
#     for i in l:
#         if i>largest:
#             largest=i
#     return largest
# a=large(l)
# print(a)

#
# Write a function to reverse a string.


# s="hello"
#
# def string(s):
#     rev=""
#     for i in s:
#         rev=i+rev
#     return rev
# a=string(s)
# print(a)


#amstrong
# def ams(n):
#     total=0
#     s=str(n)
#     l=len(s)
#     for i in s:
#         total=total+int(i)**l
#     if total==n:
#         return "amstrong"
#
#     else:
#         return "not amstrong"
# n=int(input("enter the number"))
# a=ams(n)
# print(a)


# def factor(n):
#     f=1
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
#
# factor(6)
# def factorial(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# a=factorial(6)
# print(a)
# def prime(n):
#     if n<2:
#         return "invalid"
#     c=0
#     for i in range(2,n):
#         if n%i==0:
#             c=c+1
#     if c==2:
#         return " not prime"
#
#
#     return "prime"
# a=prime(6)
# print(a)


#PALINDROME
# def palindrome(n):
#     rev=""
#     s=str(n)
#     for i in str(n):
#         rev=i+rev
#     if s==rev:
#         return "palindrome"
#
#     return " not palindrome"
#
# a=palindrome(151)
# print(a)

# s="hello"
# def string():
#     rev=""
#     for i in s:
#         rev=i+rev
#     return rev
# a=string()
# print(a)


#fibonacci
# n=12
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

#sum of digit
# n=2356
# total=0
# s=str(n)
# for i in str(n):
#     total=total+int(i)
# print(total)


# Write a function to find the largest number in a list.
# l=[1,2,4,67]
# def large(l):
#     largest = l[0]
#
#     for i in l:
#         if i>largest:
#             largest=i
#     return largest
# a=large(l)
# print(a)

# Write a function to check whether a number is prime.
#
# def prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# a=prime(7)
# print(a)

# Write a function to print all prime numbers between 1 and 100.
# for i in range(1, 101):###between 1 to 101
#     if prime(i):

#Prime numbers between two limits
# start=1
# end=100
# for i in range(start,end+1):
#     if prime(i):
#         print(i)
# 4. Count prime numbers in a list
# l=[1,2,34,5,6]
# c=0
# for i in l:
#     if prime(i):
#         c=c+1
# print(c)
# Write a function to find the sum of all prime numbers between 1 and 100
# total=0
# for i in range(1,101):
#     if prime(i):
#         total=total+i
# print(total)

# Write a function to find the largest prime number in a list.
# l = [12, 7, 25, 19, 4, 31, 10]
#
# large = 0
#
# for i in l:
#     if prime(i):
#         if i > large:
#             large = i
#
# print(large)

# 24. Write a program to remove duplicate elements from a list while maintaining the original order.
# l=[1,2,3,3,4,4,5,6,8,7,6]
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)


# 26. Write a program to separate even and odd numbers into two different lists.




# l=[1,2,3,4,5,6,7,8,9]
# new1=[]
# new2=[]
# for i in l:
#     if i%2==0:
#         new1.append(i)
#
#     else:
#         new2.append(i)
# print(new1)
# print(new2)




# 27. Write a program to find the common elements between two lists

# l1=[1,2,333,4,5]
# l2=[3,4,2]
# new=[]
# for i in l1:
#     if i in l2:
#         new.append(i)
# print(new)
# Write a function that takes a list as an
# argument and returns a new list containing only the unique elements while maintaining the original order.
# l1=[1,2,3,4,5,1,2,3,4]
# def order(l1):
#     new=[]
#     for i in l1:
#         if i not in new:
#             new.append(i)
#     return new
# a=order(l1)
# print(a)



# Write a function to count the vowels in a string.
# s="hello"
# def count(s):
#     v=0
#     for i in s:
#         if i in "AEIOUaeiou":
#             v=v+1
#     return v
# a=count(s)
# print(a)


# 15. Write a program to count the number of vowels, consonants, digits, and special characters in a string.
# s="shabna123@"
# v=0
# cos=0
# digit=0
# spcl=0
# for i in s:
#
#     if i in "AEIOUaeiou":
#         v=v+1
#     elif i.isalpha():
#         cos=cos+1
#     elif i.isdigit():
#         digit=digit+1
#     else:
#         spcl=spcl+1
# print("vowels",v)
# print("cosiquence",cos)
# print("digit",digit)
# print("spacl",spcl)


# Write a program to find the frequency of each character in a string.
# s="helloshabna"
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
#
# print(d)


# Write a program to extract only the digits from a string.
# s="abc12345@"
# new=""
# for i in s:
#     if i.isdigit():
#         new=new+i
#
# print(new)



# 20. Write a program to find the sum and average of all digits present in a string.

# s="hllo12345"
# c=0
# sum=0
# average=0
# for i in s:
#     if i.isdigit():
#         sum=sum+int(i)
#         c=c+1
# average=sum/c
# print(c)
# print(sum)
# print(average)
#
# **Question:**
# Write a Python program to create a list containing numbers from **1 to 1000**. Separate the **even numbers** and
# **odd numbers** into two different lists and find the **sum of all numbers** in the main list.

# l=[]
# l1=[]
# l2=[]
#
# for i in range(1,1001):
#     l.append(i)
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)
# print("main list",sum(l))
# print("even",l1)
# print("odd",l2)
# Write a program to count the number of words in a sentence.
# s="lam shabna hehe"
# c=0
# for i in s.split():
#     c=c+1
# print(c)
# 25. Write a program to merge two lists.
# l1=[1,2,3,4,5]
# l2=[6,7,8]
# l1.extend(l2)
# print(l1)


# Write a program to count the frequency of each word in a sentence using a dictionary.
# s="hello world good morning"
# d={}
# for i in s.split():
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

# Create a dictionary of student names and marks, then print the student with the highest mark.
# d={'anu':45,'arun':56}
# highest=0
# student=""
# for i in d:
#     if d[i] > highest:
#         highest=d[i]
#         student=i
#
# print(student)
# print(highest)

#missing and repeate

# l=[1,2,3,3,5]
# for i in range(1,len(l)+1):
#     if i not in l:
#         print("missing",i)
#         break
# for i in l:
#     if l.count(i)>1:
#         print("repeate",i)
#         break

# 36. Write a function to return the sum of all even numbers in a list.
# l=[1,2,3,4,5,6]
# def evn(l):
#     even=0
#     odd=0
#     for i in l:
#         if i%2==0:
#             even=even+i
#         else:
#             odd=odd+i
#     return even,odd
# a=evn(l)
# print(a)

# Create an Item class with item name, quantity, and price per unit, and calculate the total bill
# class Ite:
#     def __init__(self,a,q,p,t):
#         self.item_name=a
#         self.quantity=q
#         self.price=p
#         self.total=t
#
#     def show(self):
#         print("name",self.item_name,"quantity", self.quantity, "price",self.price,"total",self.total)
#     def Calculate_total(self):
#         self.total=self.price*self.quantity
#
#
# d=Ite('anu',34,2,0)
# d.Calculate_total()
# d.show()



# Create a Rectangle class to calculate the area and perimeter.
# class Rectangle:
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#
#
#     def area(self):
#
#         a=self.length*self.breadth
#         print(a)
#     def perimeter(self):
#         p=2*(self.length+self.breadth)
#
#         print(p)
#
# r=Rectangle(10,5)
# r.area()
# r.perimeter()










