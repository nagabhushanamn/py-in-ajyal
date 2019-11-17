import math


# --------------------------------------------------
# variables
# --------------------------------------------------

# --------------------------------------------------
# getting input
# --------------------------------------------------

# --------------------------------------------------
# type conversion
# --------------------------------------------------

# age calculator, 
# take birth year from Year, display display current age


# --------------------------------------------------
# string
# --------------------------------------------------


# --------------------------------------------------
# formatted string
# --------------------------------------------------


# --------------------------------------------------
# string methods
# --------------------------------------------------


# --------------------------------------------------
# operators
# --------------------------------------------------


# --------------------------------------------------
# Math functions
# --------------------------------------------------


# x= 2.9
# print(round(x))
# print(abs(-2.9))

# print(math.ceil(2.9))
# print(math.floor(2.9))


# --------------------------------------------------
# if statements
# --------------------------------------------------

# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm cloths")
# else:
#     print("It's a lovely day")


# // Ex.


"""

 price of a house is $1M

 if buyer has good credit
    they need to put down 10%
 otherwise
    they need to put down 20%   

 print the down payment       


"""


# price = 1000000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price

# print(f"Down payment : ${down_payment}")


# --------------------------------------------------
# Logical operators
# --------------------------------------------------

"""
if applicant has high_income And good credit
    Eligible for loan
"""

# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print("Elgible for loan")


# if has_high_income or has_good_credit:
#     print("Elgible for loan")

# has_criminal_record = True

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")


# --------------------------------------------------
# comparison operators
# --------------------------------------------------

# temprature = 30

# if temprature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")


# # Ex.

# name = "Nag"

# if len(name) < 3:
#     print("Name Must be at least 3 characters")
# elif len(name) > 50:
#     print("Name must be a max of 50 characters")
# else:
#     print("Name looks good")


# --------------------------------------------------
# weight convertor - project
# --------------------------------------------------


# weight = int(input("Weight: "))
# unit = input('(L)bs or (K)g: ')

# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight/0.45
#     print(f"You are {converted} pounds")


# --------------------------------------------------
# while loop
# --------------------------------------------------

# i = 1
# while i < 5:
#     print(i)
#     i = i+1
# print("Done")


# a. guess game

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if(guess == secret_number):
#         print("You won")
#         break
# else:
#     print("Sorry! You failed")


# b. car game


# command = ""
# started = False
# while command != "quit":
#     command = input("> ").lower()
#     if(command == "start"):
#         if started:
#             print("car is already started ")
#         else:
#             started = True
#             print("car started..")
#     elif command == "stop":
#         if not started:
#             print("car is already stopped")
#         else:
#             started = False
#             print("car stopped..")
#     elif command == "help":
#         print("""
#         start : to start a car
#         stop  : to stop a car
#         quit  : to exit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("i didnt understand your command")


# --------------------------------------------------
# for loop
# --------------------------------------------------

# for item in 'Python':
#     print(item)

# for item in ["nag", "indu", "riya", "diya"]:
#     print(item)

# for item in range(5,10,2):
#     print(item)


# prices=[10,20,30]
# total=0.0
# for item in prices:
#     total += item

# print(total)


# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")


# Ex.


# numbers = [5, 2, 5, 2, 2]

# for x_count in numbers:
#     output = ''
#     for y_count in range(x_count):
#         output += 'x'
#     print(output)


# --------------------------------------------------
# lists
# --------------------------------------------------

# names = ["Nag","Indu","Riya","Diya"]

# print(names)
# print(names[0])
# print(names[-2])
# print(names[2:])
# print(names[1:2])
# names[0]="Naga"
# print(names)


# Ex.


# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]

# for number in numbers:
#     if number > max:
#         max = number

# print(max)


# --------------------------------------------------
# 2d list
# --------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# --------------------------------------------------
# list methods
# --------------------------------------------------

# numbers = [5, 2, 1, 7, 4]
# numbers.append(20)
# numbers.insert(0, 20)
# numbers.pop()
# print(50 in numbers)


# remove duplicates from list

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques=[]
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)

# print(uniques)



# --------------------------------------------------
# tuple
# --------------------------------------------------


numbers=(1,2,3)



coordinates=(1,2,3)
x,y,z=coordinates # un packing




# --------------------------------------------------
# dictionaries
# --------------------------------------------------


customer={
    "name":"😎",
    "age":30,
    "is_verified":True
}

# ex. 123  - one two three


# emoji convertor

