# Conditions -> True / False
# Conditional statements -> condition use karke kaam karwana

# if else
# case statement (not in python)
# = is for assignment
# Conditional operators
"""
> greater than
< lesser than
>=
<=
== equality
!= not equals
"""

age = int(input('Enter age: '))
"""
IF age >= 18
    THEN
        OUTPUT "adult"
    ELSE
        OUTPUT "not an adult"
ENDIF            
"""

# if age <= 18:
#     print("child")
# else:
#     print('adult')
#




# if age >= 18:
#     print("adult")
# else:
#     print("not an adult")
# print("if else ended")

# boolean operators
"""
and -> returns true only if both conditions are true
or -> returns true if any one is true
not -> true-false and false-true
"""

# if (age > 18 and age != 20):
#     print("ok")
#
# if age > 15 or age == 7:
#     print("ok2")
#
# if not age > 50: # if age <= 50
#     print("ok3")

# nested if else
"""
criteria:
    - grades 80-100 -> A
    - grades 70-79 -> B
    - grades 50-69 -> C
    - failed
"""
"""
DECLARE marks : INTEGER
DECLARE grade : CHAR
OUTPUT "Enter your marks: "
INPUT marks
IF (marks >= 80) AND (marks <= 100) 
    THEN
        grade <- 'A'
    ELSE
        IF (marks >= 70) AND (marks <= 79)
            THEN
                grade <- 'B'
            ELSE
              ---       
"""
# grade = ''
# marks = int(input("Enter your marks: "))
# if marks >= 80 and marks <= 100:
#     grade = 'A'
# elif marks >= 70 and marks <= 79:
#     grade = 'B'
# elif marks >=50 and marks <=59:
#     grade='C'
# else:
#     grade=('failed')
# print("the grade of the student is",grade )




num1=int(input("enter your number"))
num2=int(input("enter your number"))
num3=int(input("enter your number"))
if num1 > num2 and num1 > num3:
    print ("num1 is the largest ")
elif num2>num1 and num2>num3:
    print("num2 is the largest")
else:
    print("num3 is the largest")





