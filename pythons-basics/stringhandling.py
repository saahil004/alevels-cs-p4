# strings
# strings is an array of character (it has indexes)
# s = "abc"
# print(s[0]) # prints a

# if 'apple' > 'banana': # strings and characters can be compared
#     print("ok") # comparision is based on ASCII codes
# else:
#     print("not ok")    
    
# def bubblesort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(i, 0, -1):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
                
# s = "apple"
# # s[0] = s[3] # strings are immutable in python
# # bubblesort(s)

# arr = []
# for i in range(len(s)):
#     arr.append(s[i])

# # alternative
# arr2 = list(s)

# bubblesort(arr)
# print(arr)      

# Q) take a string input, count how many of the characters
#   are vowels

# stri=input("enter your sentence")
# count=0
# for i in range (len(stri)):
#     if stri[i] in ['a', 'e', 'i', 'o', 'u']:
#         count+=1
# print("counts of vowels is",count)        
           
# converting a list into a string
# arr = ['h', 'e', 'l', 'l', 'o', '!']
# s = "".join(arr)
# print(s)

# option 2: + is used to concatinate strings
# s1 = "hello"
# s2 = "world"
# s3 = s1 + " " + s2
# print(s3)

# s = ""
# arr = ['h', 'e', 'l', 'l', 'o', '!']
# for i in range(len(arr)):
#     s += arr[i]

# print(s)    


# multiplying a number by string
# s = 'hi'
# num = 5
# s2 = s * num
# print(s2)

# sentence = "hello,this,is,computer,science"
# words = sentence.split(',')
# print(words)

# Indexing
# s = "Hello world"
# print(s[0:7:2])

# s = 'Saahil Ghulam'
# fname = s[0:6]
# lname = s[::-1]
# print(fname)
# print(lname)


# s = "hello".upper()        # 'HELLO'
# print(s)
# s = "HELLO".lower()         # 'hello'
# print(s)
# s = "hello world".title()   # 'Hello World'
# print(s)
# s = "Hello World".swapcase()# 'hELLO wORLD'
# print(s)
# s = "hello".capitalize()    # 'Hello'
# print(s)

# s = '23'
# flag = s.isdigit()
# print(flag)

#P
#"
#Programming
#nuF si gnimmargrop
#rgamn

# if "Programming">"programming":
