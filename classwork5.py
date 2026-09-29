d = {'a':23,'b':25,'c':28,'d':30,'e':22}

# Even values
for value in d.values():
    if value % 2 == 0:
        print(value)


colors = ['red','green','blue','orange','black']

# Starting letter
for color in colors:
    print(color[0])

# Last letter
for color in colors:
    print(color[-1])

# Reverse
for color in colors:
    print(color[::-1])

# All colors containing letter 'b'
for color in colors:
    if 'b' in color:
        print(color)

#Range function
# 100-200
for i in range(100, 201):
    print(i)

# 1,2,3,4,5
for i in range(1, 6):
    print(i)

# 1,3,5,7,9,11
for i in range(1, 12, 2):
    print(i)

# 2,4,6,8,10
for i in range(2, 11, 2):
    print(i)

# 100,200,300,400,500
for i in range(100, 501, 100):
    print(i)

# 5,4,3,2,1
for i in range(5, 0, -1):
    print(i)

# 3,6,9,12,15,18,21
for i in range(3, 22, 3):
    print(i)

# 1,4,9,16,25,36 (Squares)
for i in range(1, 7):
    print(i ** 2)

# print all 3 digit numbers range(100,999)
for i in range(100, 999):
    print(i)


#Print all numbers divisible by 3 in the range 100–200
for i in range(100, 201):
    if i % 3 == 0:
        print(i)
#Print cubes: 1, 8, 27, 64, 125
for i in range(1, 6):
    print(i ** 3)