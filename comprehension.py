# definition:-
#[ this is a simple and easy syntax for creating a new sequence from the given iterable (sequence)]
#3 type
#list comprehension
#set

##list comprehension

# syntax:
# new_list=[output/exp for item n iterable if conditoin(optional)]

##set comprehension
# new_list={output/exp for item n iterable if conditoin(optional)}

##dictoinary comprehension
# new_list={key:value for item n iterable if conditoin(optional)}

#give list
# l=[1,2,3,4]     #each iteration  adds i**2 where i take values from the sequences l
# new=[i**2 for i in l]
# print(new)

#create a new list with cubes of each element
# new=[i**3 for i in l]
# print(new)

# new=[5 for i in l]
# print(new)


#give list
# l=[23,46,55,11,78,90,24]
#create a new list with even values
# new=[i for in l if i%2==0]
# print(new)

# new=[i for i in l if i>50]
# print(new)




#Given  a list colors=['red','green','blue','orange']
colors=['red','green','blue','orange']
# create a new list with first letter of each color

# new=[i[0] for i in colors ]
# print(new)
# create a new list with length of each color
# new=[len(i) for i in colors]
# print(new)


# #create new list with number
# new=[i[0] for i in colors]

#2
#create a new list of square roots
# l=[25,36,81,100]
# import math
# new=[math.sqrt(i) for i in l]
# print(new)
# c=['red','green','blue','yellow','black']
# #create a new list of first characters
# new=[i[0] for i in c]
# print(new)
# #create a new list of last characters
# new=[i[-1] for i in c]
# print(new)
# #create a new list of reverse of each elemnt
# new=[i[::-1] for i in c]
# print(new)

#Given a list l=[23,78,12,56]
#Add 10 to each element in the given sequence

##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
# {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
# {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
# new=[i['email'] for i in l]
# print(new)



# #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # create a list of names
# new=[i for i in d]
# print(new)
# # # create a list of marks
# new=[i for i in d.values()]
# print(new)

#
# #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

# #create a list of string values
# new=[i for i in l if type(i)==str]
# print(new)
# # #create a list of floats
# new=[i for i in l if type(i)==float]
# print(new)
# # #create a list of positive numbers
# new=[i for i in l if type(i)!=str and i>0]
# print(new)

# #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# #create a new list with elements whose length is greater than 6
# new=[i for i in fruits if len(i)>6]
# print(new)
# # #create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[i for i in range(1,101) if i%3==0]
# print(new)
# Given s="python coding  is easy and fun"
# # create a new list with only vowels
# new=[i for i in s if i in "aeiouAEIOU"]
# print(new)


#set comprehension

# s="python coding  is easy and fun"
# # # create a new list with only vowels
#
# new={i for i in s if i in "aeiouAEIOU"}
# print(new)


#dictionary  comprehention
#given list
# l=[1,2,3,4]
#create a new dic wherekey are no and values the square of each number
# new={i:i**2 for i in l}
# print(new)

#create a new dic wherekey are no and values the square of each number
# new={i:i**3 for i in l}
# print(new)


#given list
# l=[10,20,30,40]
#crete a new dic where keys are index and values are number itself
# new={i:l[i] for i in range(0,len(l))}
# print(new)


#given string
# s="python coding  is easy and fun"

#crete a new dic where keys are words and values are length of each word
# new={i:len(i) for i in s.split()}
# print(new)


