# Filing
"""
Modes:
1) Read -> only reading data from the file
2) Write -> create / overwrite
3) Append -> writes from the end of file
"""

"""
Reading Process:
1) open file
2) read each line
3) when end of file arrives -> end
4) file close
"""

"""
Filing Functions:
- file = open("file name", "mode(r,w,a)") -> open creates a file obj
- content = file.read() -> stores whole content in "content"
- line = file.readline() -> returns one line of the file
- file.close() -> closes the file
- end of file condition -> readline returns an empty string
"""


# file = open("reading.txt", "r")
# c = file.read()
# print(c)

# Store each name in the array
# file = open("reading.txt", "r")
# names = []
# for line in file:
#     names.append(line.strip())
# print(names)    
# file.close()

# Only use for line in file when you want to read one line at a time -> else use while loop


# file = open("reading.txt", "r")
# names = []
# line = file.readline().strip()
# while line != "":
#     names.append(line)
#     line = file.readline().strip()
# print(names)    
# file.close()


# chars = ["a", "b"]
# print(chars)
# chars.append("c")
# print(chars)


# Case 2: Record on separate lines

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def SetName(self, n):
        self.__name = n
            
    def SetAge(self, a):
        self.__age = a
    
    def GetName(self):
        return self.__name
            
    def GetAge(self):
        return self.__age        
    
# students = []
# file = open("reading2.txt", "r")
# name = file.readline().strip()
# age = file.readline().strip() 
# while name != "" and age != "":
#     s = Student(name, int(age))
#     students.append(s)   
#     name = file.readline().strip()
#     age = file.readline().strip()
# file.close()
# for i in range(len(students)):
#     print("Student name: ", students[i].GetName())   
#     print("Student age: ", students[i].GetAge())
       
       
# Case 3: Comma separated values
"""
Split function revision
"""       
# s = "I,love,studying,computer,science"
# arr = s.split(",")
# print(arr)

# students = []
# file = open("reading3.txt", "r")
# for line in file:
#     arr = line.strip().split(",")
#     s = Student(arr[0], int(arr[1]))
#     students.append(s)
# file.close()
# for i in range(len(students)):
#     print("Student name: ", students[i].GetName())   
#     print("Student age: ", students[i].GetAge())
       
    
students = []
file = open("reading3.txt", "r")
line = file.readline().strip()
while line != "":
    arr = line.split(",")
    s = Student(arr[0], int(arr[1]))
    students.append(s)
    line = file.readline().strip()
file.close()
for i in range(len(students)):
    print("Student name: ", students[i].GetName())   
    print("Student age: ", students[i].GetAge())
       