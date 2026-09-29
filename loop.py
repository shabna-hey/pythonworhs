#looping statement

#while loop


#1)write a prgm to print first 10 integers.
# i=1
# while i<=10:
#     print(i,end=" , ")
#     i+=1

#2)write a progm to print first 10 even numbers

# i=2
# while i<=20:
#     print(i,end=" , ")
#     i+=2


#3)write a prgm to prtint odd numbers

# i=1
# while i<=19:
#     print(i,end=" , ")
#     i+=2

#1,4,7,10,13,16

#i=1
# while i<=16:
#     print(i,end=" , ")
#     i+=3

# #10,20,30,40,50,60,70,80
# i=10
# while i<=80:
#     print(i,end=" , ")
#     i+=10


#3,6,9,12,15,18,21

# # i=3
# # while i<=21:
# #     print(i,end=" , ")
# #     i+=3


#5,4,3,2,1
# i=5
# while i>=1:
#     print(i,end=" , ")
#     i-=1

#8,6,4,2,0

# i=8
# while i>=0:
#     print(i,end=" , ")
#     i-=2


#print all 4 digit number (1000-9999)
# i=1000
# while i<=9999:
#     print(i,end=" , ")
#     i+=1

#print those 3 digit numbers that are divisible by 3
# i=100
# while i<=999:
#     if i%3==0:
#         print(i,end=" , ")
#     i+=1

#print those 4 digit number that contain digit '3' (# in operator-seqence)
# i=1000
# while i<=9999:
#     s=str(i)
#     if '3'in s:
#         print(s,end=" , ")
#     i+=1


#print those numbers thst are divisible by 3 and 5 in range(1,100)
# i=1
# while i<=100:
#     if i%3==0 and  i%5==0:i=1000
# while i<=9999:
#      s=str(i)
#      if s in 3:
#         print(s,end=" , ")
#      i+=1
#      print(i, end=" , ")
#     i+=1


#1,4,9,16,25,36,49,64,81,100
# i=1
# while i<=10:
#     print(i**2,end=" , ")
#     i+=1

# print those 3 digit numbers that contains '3 digit"

# i=1000
# while i<=9999:
#      s=str(i)
#      if '3' in s:
#         print(s,end=" , ")
#      i+=1

#count of those 3 digit numbers that contain digit'3'

# count=0
# i=100
# while i<=999:
#     s=str(i)
#     if '3' in s:
#         count=count+1
#     i+=1
# print(count)

#count of those numbers that are divisible by 7 or 3 in the range (200-300)

#count of those odd numbers that are divisible by 5 in the range (1,100)
# count=0
# i=1
# while i<=100:
#     if i%2!=0:
#         if i%5==0:
#             count=count+1
#     i+=1
# print(count)

#count of all palindrome numbers in range (1,1000)
# count=0
# i=1
# while i<=100:
#    s=str(i)
#    if (s==s[::-1]):
#        count=count+1
#         #print(s)
#    i+=1
# print(count)

#count of those no that are divisible by 3 in range of(1,50)

# count=0
# i=1
# while i<=50:
#     s=str(i)
#     if i%3==0:
#         print(i)
#         count=count+1
#     i+=1
# print(count)

#sum of those no that are divisible by 3 in the range (1,100)
# s=0
# i=1
# while i<=100:
#     if i%3==0:
#         s+=1
#     i+=1
# print(s)


#find the sum of first 5 numbers 1+2+3+4+5
# s=0
# i=1
# while i<=5:
#     s+=1
#     i+=1
# print(s)


# sum of all 3 digit number
# s=0
# i=100
# while i<=999:
#     s+=i
#     i+=1
# print(s)

#sum of first 10 even numbers
# s=0
# i=2
# while i<=20:
#     s+=i
#     i+=2
# print(s)
#

#product of series 1,2,3,4,5product=1
# i=1
# while i<=19:
#     product*=i
#     i+=2
# print(product)
# product=1
# i=1
# while i<=5:
#     product*=i
#     i+=1
# print(product)


#product of  first 10 odd numbers

#

#product of numbers that contaian  digit '3' in the range (1,50)

# p=1
# i=1
# while i<=50:
#     s=str(i)
#     if '3' in s:
#         p*=i
#     i+=1
# print(p)
#


#factorial of a no entered by user  (5!=5*4*3*2*1)
# n=int(input("enter the no"))
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

#multiplication table of a number(up to 10)
# n=int(input("enter the no of table:"))
# i=1
# p=1
# while i<=10:
#     p=i*n
#     print(i, "*" ,n, "=",p )
#     i+=1


#sum of digit 135=1+3+5

# n=int(input("enter the no:"))
# s=0
# while n>0:
#     d=n%10
#     s=s+d
#     n=n//10
# print(s)


# i=100
# while i<=999:
#     print(i)
#     i+=1



# for i in range(100,999):
#     print(i,end=" ")


