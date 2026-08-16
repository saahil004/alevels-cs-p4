# Arrays -> indexed collection of same datatype (not in python)
# List -> indexed collection of different datatype
# Array -> fixed size
# List -> dynamic sizing


#         0   1    2   3  4   5
marks1 = [10, 20, 30, 50, 80, 70] # n = 6

marks2 = [10, 20, 'hi', 50, 80, 'hello'] # not an array, list

print("First array: ", marks1)
print("Second array: ", marks2)

# indexes start from zero
print("Marks of third student is: ", marks1[2])
std1 = marks1[0]
std5 = marks1[4]

# Length of an array
n = len(marks1)
print(n)

age = 10
print(type(age).__name__)




# Make an array of 10 elements (random numbers),
# print length of the array, and the array
# then print array from index 3 to index 5

# slicing -> upperbound is exclusive
print(marks1[3 : 6]) # prints values at index 3 4 5

# Making an array wihtout knowing the values

# Pseudocode
# DECLARE marks : ARRAY[1 : 15] OF INTEGER

marks = [None, None, None, None]
print(len(marks))

# marks1[6] = 55 # index out of bounds error

# appending an element at the end of an array
marks1.append(55)
print(marks1)

val = marks1.pop() # removes an element from the end of an array
print(marks1,' Value popped: ', val)

# remove element at index 2
val2 = marks1.pop(2)
print(marks1, " value popped: ", val2)


# Activity
"""
1) create an array of 10 elements named marks
2) print whole array and the length of the array
3) now add 44 at the end of the array and then print the array
    with new length
4) then remove the value at index 3 and print the popped value
5) take input the value at 8th index 
6) print the name of datatype of 4th element    
    
"""



