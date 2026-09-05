# Loops
"""
Types of loops in python
1) for loop / for each loop
2) while loop

Nested loop -> loop inside a loop
"""
# range function
# range(start num, end num + 1, step)

# range(1, 6, 2)
# range(1, 6) # step by default 1
# range(5) # start by default zero and step 1

"""
FOR i <- 1 TO 10
    <>
    <>
    <>
NEXT i    
"""

# for i in range(1, 6, 1):
#     print(i)
#     print("Loop ended")

# for i in range(6):
#     print("Index value: ", i)

# for i in range(1, 8):
#     print("Index value: ", i)

#        0   1   2   3   4
marks = [44, 22, 11, 50, 40]
for i in range(5):
    print("Value at index: ", i, " is ", marks[i])

# for i in range(len(marks)):


# Activity
"""
Q) total the marks, calculate average... print both
   for each student, if the marks are above 30, print passed with
   A grade, if student has marks above 20, print passed with B grade
   else print student has failed
"""
# total = 0
# for i in range(5):
#     total += marks[i]
#     if marks[i] >= 30:
#         print("Student ", i, " passed with A grade")
#     elif marks[i] >= 20:
#         print("Student ", i, " passed with B grade")
#     else:
#         print("Student ", i, " has failed")
# avg = total / 5
# print("Total marks: ", total)
# print("Average marks: ", avg)

# For each loop -> loops at values directly
# t = 0
# for mark in marks:
#     t += mark

# While loop
"""
WHILE (CONDITION) DO
    <>
    <>
    <>
ENDWHILE    
"""
# x = 5
# while x > 1:
#     print(x)
#     x = x - 1

# Activity
"""
"""

max=0
for i in range(5):
    num=int(input("enter your numbers"))
    if num>max:
        max=num
print("the largest number is",max)

oddcount=0
evencount=0
for i in range(10):
    num=int(input("enter your number"))
    if num % 2==0:
        evencount=evencount+1
    else:
        oddcount=oddcount+1
print("the oddcount of the number is",oddcount)
print("the evencount of the numbers is",evencount)



