# d={'shabna':23,'anu':45,'ester':67}
### Dictionary Programming Questions

#Create a dictionary where keys are words and values are the length of each word

# for i in d:
#     d[i]=len(i)
# print(d)

# 2. Create a dictionary where keys are numbers and values are their squares.

# l=[2,3,4,5]
# d={}
# for i in l:
#     d[i]=i**2
# print(d)
#
# 3. Create a dictionary where keys are numbers and values are their cubes.
# l=[6,7,8,9]
# d={}
# for i in l:
#     d[i]=i**3
# print(d)
# 4. Create a dictionary containing each word and its frequency in a sentence.
# s="apple  banana  apple  apple  orange"
# d={}
# for i in s.split():
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

# 5. Create a dictionary containing each character and its frequency in a string.
# s="hello world"
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

#
# 6. Create a dictionary containing numbers and whether they are even or odd.
# l=[2,3,4,5,6]
# d={}
# for i in l:
#     if i%2==0:
#         d[i]="even"
#     else:
#         d[i]="odd"
#         d[i]="even"
# print(d)

# 7. Create a new dictionary containing only the values greater than 50.
#
# s={'manu':20,'fhe':56,'loi':90}
# d={}
# for i in s:
#     if s[i]>50:
#         d[i]=s[i]
# print(d)



# 8. Create a new dictionary containing only the even values.

# s=[2,34,5,6,7,8]
# d={}
# for i in s:
#     if i%2==0:
#         d[i]=i
#
#
# 
# print(d)
#
# 9. Create a dictionary from two given lists.

# l1=['a','b','c']
# l2=[23,34,21]
# d={}
# for i in range(len(l1)):
#     d[l1[i]]=l2[i]
#
# print(d)
#
# 10. Create a new dictionary containing student names and their marks.

# s=['anu','meenu','kaks']
# m=[50,45,23]
# d={}
# for i in range(len(s)):
#     d[s[i]]=m[i]
# print(d)
# value=list(d.values())
#
# 11. Create a new dictionary containing employee names and their salaries.
# e=['menu','raju','kalu','rohini','ammu']
# s=[2300,40000,50000,90000,56000]
# d={}
# for i in range(len(e)):
#     d[e[i]]=s[i]
# print(d)
#Find the key having the largest value in a dictionary.
#d={'menu': 2300, 'raju': 40000, 'kalu': 50000, 'rohini': 90000, 'ammu': 56000}
# max_value = 0
# #
# for key in d:
#      if d[key] > max_value:
#          max_value = d[key]
#          max_key = key
#
# print(max_key)
# 13. Find the key having the smallest value in a dictionary.
#
# min_value=9999
# for i in d:
#     if d[i]<min_value:
#         min_value=d[i]
#         min_key=i
# print(min_key)

# values=list(d.values())
# values.sort()
# print("small",values[0])


# 14. Find the largest and second-largest values in a dictionary.
# value=list(d.values())
# value.sort()
# print("largest",value[0])
# print("second",value[-2])
# #
# # 15. Find the smallest and second-smallest values in a dictionary.
# value=list(d.values())
# value.sort()
# print("smallest",value[0])
# print("second_smallest",value[1])
#
# 16. Find the sum of all values in a dictionary.
#
# 17. Find the average of all values in a dictionary.
#
# 18. Count the number of keys and values in a dictionary.
#
# 19. Remove duplicate values from a dictionary.
# d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
#
# s = {}
#
# for i in d:
#     if d[i] not in s.values():
#         s[i] = d[i]
#
# print(s)
#
# 20. Merge two dictionaries into a single dictionary.
# d1 = {'a': 10, 'b': 20}
# d2 = {'c': 30, 'd': 40}
#
# d1.update(d2)
# print(d1)
