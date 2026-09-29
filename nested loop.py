#nested loop
from email.contentmanager import raw_data_manager

# l=[10,20,30,40]
# for i in l:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#---------------------------------------------------#pattern-------------------------------------------------------------------------------

#111
#222
#333
# for i in range(1,4):
#     for j in range (1,4):
#         print(i,end=" ")
#     print()
#---------------------------------------------------
#1 2 3
#1 2 3
#1 2 3
# for i in range(1,4):
#     for j in range (1,4):
#         print(j,end=" ")
#     print()

#---------------------------------------------------------------------------

#l=[['lion','tiger'],['cat','elephat']]
# l=[['lion','tiger'],['cat','elephat']]
# for i in l:
#     for j in i:
#         print(j)

#------------------------------------------
#n=['kelly','allan','jenny']
#print pattern
#eg;  kelly kelly
      #allan allan allan
      #jenny jenny jenny
# for i in n:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()
#----------------------------------------------------------------------------------------------------------------------------------
#given 2 list
# n=[1,2,3]
# s=['what','why','when']
# #ans =[what,when,why]
# for i in n:
#     print(i)
#     for j in s:
#         print(j,end=" ")
#     print()

#-----------------------------------------------------------------------------------------------------------------------------------------

#given  a list   #each value print

# d={'id':101,'name':'arun','age':24},{'id':102,'name':'amal','age':23},{'id':101,'name':'aysha','age':20}
#
# for i in d:
#     print(i)
#     for j in i.values():
#         print(j,end=" ")
#     print()


#-------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------pattern-----------------------------------------------------------------------------------------



#* * * *
#* * * *
#* * * *

# for i in range(1,4):
#     for i in range(1,5):
#         print('*',end=" ")
#     print()



#   *
#   * *
#   * * *
#   * * * *

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()



#2 2 2 2
#4 4 4 4
#6 6 6 6
#8 8 8 8#
# for i in range(2,9,2):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()



#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1
#
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#

# * * * *
# * * *
# * *
# *

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()


# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()


# 1000
# 0200
# 0030
# 0004

# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end=" ")
#         else:
#             print(0,end=" ")
#     print()


# 1
# 10
# 101
# 1010
# for i in range(1,5):
#     for j in range(1,i+1):
#         if(j%2==1):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()


# 1
# 4 9
# 16 25 36
# 49 64 81 100

# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num**2,end=" ")
#         num+=1
#     print()


# 1
# 3 5
# 7 9 11
# 13 15 17 19

# k=1
# for i in range(1,5):
#      for j in range(i):
#          print(k,end=" ")
#          k+=2
#      print()


# 2
# 4 6
# 8 10 12
# 14 16 18 20

# num=2
# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ")
#         num+=2
#     print()

# 1 2 3 4
# 1 2 3
# 1 2
# 1
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# 10 9 8 7
# 6 5 4
# 3 2
# 1
# num=10
# for i in range(4,0,-1):
#     for j in range(i):
#         print(num,end=" ")
#         num-=1
#     print()

# A
# B C
# D E F
# G H I j


# letter=ord('A')
# for i in range(1,5):
#      for j in range(i):
#          print(chr(letter),end=" ")
#          letter+=1
#      print()
#reverse

# letter = 65
# for i in range(5,0,-1):
#     for j in range(i):
#         print(chr(letter), end=" ")
#         letter += 1
#     print()

#    1
#   2 3
#  4 5 6
# 7 8 9 10

# num=1
# for i in range(1,5):
#     #space
#     for j in range(4-i):
#         print("",end=" ")
#     #number
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()





# *
# ***
# *****
# *******

# for i in range(1,8,2):
#     for j in range(i):
#         print('*',end=" ")
#     print()



# for i in range(2,9,2):
#      for j in range(i):
#          print('*',end=" ")
#      print()
#A
#A A A
#
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     K+=1
#     print()






# l=[23,65,42,80,56,41] #print all each number
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
#     print()



#print all prime numbers in the range(1,100)

# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")



#print all amstrong numbers in the range(100,1000)

# for i in range(100,1000):
#     sum=0
#     s=str(i)
#     l=len(s)
#     for j in s:
#      sum=sum+int(j)**l
#      if sum==i:
#         print(i)

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#
#     for j in range(1,i+1):
#         print('*',end="  ")
#     k=k-2
#     print()

#-------------------------------------------------------------------------------------------------------------------------------------------
# *
# * *
# * * *
# * * * *
# * *
# *

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for k in range(5,0,-1):
#     for h in range(i,k+1):
#         print('*',end=" ")
#     print()


#




# k=6
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     k=k+2
#     for j in range()








#E
#D D
#C C C
#B B B B
#A A A A A
# l=ord('E')
# for i in range(1,6):
#     print(" ",end=" ")
#     for j in range(1,i+1):
#         print(chr(l),end=" ")
#     l-=1
#     print()
# 1
# 21
# 321
# 4321

# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     i+=1
#     print()
#
# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1
# for i in range(5,0,-1):
#      for j in range(6,i,-1):
#          print(i,end=" ")
#      print()


# 1 1 1 1 1
#   2 2 2 2
#     3 3 3
#       4 4
#         5

# for i in range(1, 6):
#     print("  " * (i - 1), end="")
#     for j in range(6 - i):
#         print(i, end=" ")
#     print()
# n=153
def amstrong(n):
    sum=0
    s=str(n)
    l=len(s)
    for i in s:
        sum=sum+int(i)**l
    if sum==n:
        return "amstrong"
    else:
        return "not amstrong"

for i in range(1,1001):
    if amstrong(n):
        print(n)




