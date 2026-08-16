# Datatypes
"""
1) INTEGER -> int -> whole numbers eg; 24, -24, 0
2) REAL -> float -> decimal values eg; 0.2, -0.2, 0.023
3) STRING -> str -> sentence, word, anything in "" eg; "hello", '24', 'c'
4) CHAR -> char -> single character eg, 'a', ' ', '3'
5) BOOLEAN -> bool -> True or False
"""

# Variables and datatypes
# DECLARE age : INTEGER
age = 0 # integer variable

# DECLARE name : STRING
name1 = ''
name2 = 'saahil'

# DECLARE weight : REAL
weight = 0.0

# DECLARE chr : CHAR
ch = 'a'

# DECLARE studiesMath : BOOLEAN
studiesMath = True # student studies math
studiesMath = False # student does not study math




# Activity 1
"""
Q) declare variables and store your height, age, name, 
  your grade in cs, and whether you like math or not
"""

# answer
"""
height = 0.00
age = 0
name = ""
grade = 'A'
mathslike = False
"""


# Mathematical operators
"""
+ -> add two or more values
- -> subtract two or more values
* -> multiply
/ -> divide
() -> grouping
** -> power     pseudocode: 2^6    code: 2**6
% -> mod (remainder)
// -> div (answer of division in whole number)
"""

# x = 5
# y = 2
# z = True
# p = (x ** y) % 4
# print("the value of p: ", p)



# Activity
"""
Q) Define length of a rectangle as 10, width as 3, height as 12
    and then calculate total surface area and volume
    then output both using different prints and with a 
        suitable message
"""

"""
l = 10
w =  3
h = 12
Sa = 2*(l*w)+2*(l*h)+2*(w*h)
v = l*w*h
print('Surface area is:', Sa)
print('Volume is: ', v)
"""


# printing
# print("Hello world")
# print(x)
# print(z)
# print("the value of x is: ", x, " z is ", z)

# user inputs
# python takes string input, we typecast in integer
# age = input('Enter name: ')
# print('Your age times 4 is: ', age * 4)

# studentwt = float(input("Enter weight: "))
# print(studentwt * 1.1)
#
# studentname = input("Enter your name: ")
# print(studentname)


# Activity
"""
Q) take input name, age, gender, and marks.
    upgrade the marks by 20% and then
    print all details and updated marks
"""
# name = input("enter your name:")
# age = int(input("enter your age:"))
# gender = input("whats your gender:")
# marks = int(input('enter your marks:'))
# marks = marks * 1.2
# print(name)
# print(age)
# print(gender)
# print(marks)


age = 10
if type(age).__name__ == 'int':
    print('INTEGER Datatype')
else:
    print("Undefined")

# type(<variable>) -> returns object of datatype
# type(<variable>).__name__ -> returns name of the datatype


























