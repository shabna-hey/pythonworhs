#map
#create a new list of square
#map(function,sequence)
#l=[1,2,3,4]
# print(list(map(lambda a:a**2,l)))
# print(set(map(lambda a:a**2,l)))
# print(tuple(map(lambda a:a**2,l)))

#crete a new list of cubes
# print(list(map(lambda a:a**3,l)))
#create a new list of square roots


# l=[25,36,81,100]
#
# print(list(map(lambda a:a**0.5,l)))



# colors=['red','green','blue','yellow','black']
#create a new list of lengths
# print(list(map(lambda a:len(a),colors)))
#create a new list of first characters
# print(list(map(lambda a:a[0],colors)))
#create a new list of last characters
# print(list(map(lambda a:a[-1],colors)))
#
#create a new list of reverse of each elemnt
# print(list(map(lambda a:a[::-1],colors)))
#
# l=[23,78,12,56]
#Add 10 to each element in the given sequence
# print(list(map(lambda a:a+10,l)))

##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
# {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
# {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
# print(list(map(lambda x:x['email'],l)))


######FILTER#######
#even numbers
# l=[1,2,3,4,5,6,7,8,9,10]

# print(list(filter(lambda a:a%2==0,l)))

#odd numbers

# print(list(filter(lambda a:a%2!=0,l)))

# l=[23,65,89,12,20,33,85,40]
# #filter elements grether than 50
# print(list(filter(lambda a:a>50,l)))
# #filter even values less than 50
# print(list(filter(lambda n:n%2==0 and n<50,l)))
# f=['apple','orange','pineapple','grapes','avacado']
# #filter the element whose length is greather than 5
# print(list(filter(lambda b:len(b)>5,f)))



###REDUCE######


# #sum of a list
# l=[1,2,3,4]
# import functools
# print(functools.reduce(lambda a,b:a+b,l,0))
# #product
# print(functools.reduce(lambda a,b:a*b,l,1))

