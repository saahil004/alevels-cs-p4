# Filing
"""
- permanent storage

Modes:
- read -> only to read data from a file
- write -> create a new file / overwrite an existing
- append -> writes from the end of file

Basic flow (past papers) -> file -> array of objects -> functions
"""

# opening a file    file = open("filename", "mode(r,w,a)")
# filename = "filing.txt"
# file = open(filename, "w") # to create a file

# for i in range(10):
#     line = "hello world " + str(i) + "\n"
#     file.write(line)

# file.close()    
    
    
    
    
# file = open("filing.txt", "r")
# for line in file:
    # print(line.strip())
# s = file.read() # read reads the whole file in one go
# print(s)

# line = file.readline().strip()
# while line != "":
#     print(line)
#     line = file.readline().strip()
    
# file.close()  

# arr = [1,2,3,4,5]
# # print(arr[100])
# try:
#     print(arr[100])
# except Exception as e:
#     print("Something went wrong: ", str(e))
        








# file = open("filing.txt", "a")
# line = "HELLO WORLD 200" + "\n"
# file.write(line)
# file.close()
# file = open("filing.txt", "r")
# line = file.readline().strip()
# while line != "":
#     print(line)
#     line = file.readline().strip()
    
# file.close() 

class Student:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        
    def getId(self):
        return self.__id    
    
    def getName(self):
        return self.__name    
    
# Q) read all students from filing.txt and make a new file 
# after deleting the student with id 2

# read, new file, add only students with id that is not 2

# file = open("filing.txt", "r")
# students = []
# for line in file:
#     idname = line.strip().split(',')
#     s = Student(int(idname[0]), idname[1])
#     students.append(s)

# file.close()

# # for i in range(len(students)):
# #     print(students[i].getName())    

# file = open("updated.txt", "w")
# for i in range(len(students)):
#     if students[i].getId() != 2:
#         line = str(students[i].getId()) + "," + students[i].getName() + "\n"
#         file.write(line)

# file.close()      


# file = open("filing.txt", "r")
# arr = []

# id = file.readline().strip()
# name = file.readline().strip()
# while id != "" and name != "":
#     s = Student(int(id), name)
#     arr.append(s)
#     id = file.readline().strip()
#     name = file.readline().strip()

# file.close()
# # for s in arr:
# #     print(s.getName())

# file = open("updated.txt", "w")
# for i in range(len(arr)):
#    if arr[i].getId() % 2 == 0: 
#     file.write(str(arr[i].getId()) + "\n")
#     file.write(str(arr[i].getName()) + "\n")
# file.close()    
        


# exception handling
try:
  file = open("filing.txt", "r")
  print(file.read())
  file.close()
except IOError as e:
    print(str(e))  
finally:
    print("Try except done")

 
