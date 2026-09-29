
#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese






# weight = float(input("Enter weight : "))
# height = float(input("Enter height : "))
#
# bmi = weight / (height ** 2)
#
# print("BMI =", round(bmi, 2))
#
# if bmi <= 18:
#     print("Status: Underweight")
# elif bmi <= 25:
#     print("Status: Normal")
# elif bmi <= 40:
#     print("Status: Overweight")
# else:
#     print("Status: Obese")

#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.



# Toy Vendor Discount

# product= int(input("Enter product (1-Battery, 2-Key, 3-Electrical): "))
# amount = int(input("Enter order amount: "))
# discount = 0
# if product== 1:
#      if amount > 1000:
#          discount =amount - (amount * 10 / 100)
        #print("net amount", amount)
# elif product== 2:
#         if amount > 100:
#          discount = amount -  (amount * 5 /100)
        #print("net amount", amount)
# elif product== 3:
#      if amount > 500:
#          discount = amount -  (amount * 10 / 100)
        #print("net amount", amount)
# else:
#      print("Invalid product code")

#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

# FizzBuzz

# num = int(input("Enter a number: "))
#
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)