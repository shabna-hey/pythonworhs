#even or odd
from hmac import new

# def odd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
#
# s=int(input("enter number"))
# a=odd(s)
# print(a)





#sum of two number
# def number(n1,n2):
#
#      s=n1+n2
#      return s
# n1=int(input("enter the number"))
# n2=int(input("enter the 2number"))
# a=number(n1,n2)
# print(a)



#prime

# def prime(n):
#     if n<2:
#         return "not prime"
#     for i in range(2,n):
#             if n%i==0:
#                 return "not prime"
#
#     return "prime"
# n=int(input("enter a no"))
# a=prime(n)
# print(a)

#even
# l=[2,20,68,4,42,3,9]
# def even(l):
#     new=[]
#     for i in l:
#         if i%2==0:
#             new.append(i)
#     return new
# a=even(l)
# print(a)


# l1=[20,30,40,50]
# l2=[20,34,40,60]
# def common(l1,l2):
#     new=[]
#     for i in l1:
#         if i in l2:
#             new.append(i)
#     return new
# a=common(l1,l2)
# print(a)

#number is palindrome or not
# def palindrome(n):
#     rev=""
#     s=str(n)
#     for i in s:
#
#         rev=i+rev
#     if s==rev:
#             return "palindrome"
#     else:
#             return "not palindrome"
#
# d=int(input("enter the digit"))
# a=palindrome(d)
# print(a)
#
#
#
# def palindrome_s(n):
#     rev=""
#     for i in str(n):
#         rev=i+rev
#
#     if s==rev:
#         return "palindrome"
#     else:
#         return "not palindrome"
# s=input("enter string")
# a=palindrome_s(s)
# print(a)


# d={'arun':45,'shabna':55,'eleen':67}
# def dictionary():
#     new={}
#     for k,v in d.items():
#         if v>50:
#             new[k]=v
#     return new
# a=dictionary()
# print(a)

#factorial
# def fact_n(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# a=int(input("enter the number"))
# b=fact_n(a)
# print(b)

# def number_n(n):
#     sum=0
#     s=str(n)
#     l=len(s)
#     for i in s:
#         sum=sum+int(i)**l
#     if sum==n:
#             return "armstrong"
#     else:
#             return "not armstrong"
#
# n=int(input("enter the number"))
# a=number_n(n)
# print(a)

# def factor(n):
#     fact=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             fact.append(i)
#     return fact
# n=int(input("enter factor"))
# a=factor(n)
# print(a)

#sum of digits
# def digits(n):
#     sum=0
#     s=str(n)
#     for i in s:
#         sum=sum+int(i)
#
#     return sum
# n=int(input("enter digit"))
# a=digits(n)
# print(a)




# def reverse_n(n):
#     rev = ""
#
#     for i in str(n):
#         rev = i + rev
#
#     return rev
#
#
# n = int(input("Enter the number: "))
# a = reverse_n(n)
# print(a)



















