# 2D arrays
"""
Array inside an array
other way to look at it: rows and columns
"""

# how to declare a 2d array
# arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# arr[2][2] = 3000
# print(arr[0]) # prints only the first array element

# how to declare an empty array 10 rows, 2 columns
# arr = [[None for i in range(2)] for j in range(10)]
# print(arr)

arr = [
    [3, 11, 2, 42],
    [13, 112, 11, 412],
    [311, 121, 111, 4112]
]

# print(len(arr))

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j])

# totalling whole array
# total = 0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         total += arr[i][j]
# print(total)        

# totalling row
# total = 0
# for i in range(len(arr[0])):
#     total += arr[0][i]
    
# [13, 112, 11, 412] total = 0  
    
#total = 0
#for i in range(len(arr)): 
    # for j in range(len(arr[i])):
    #     total += arr[i][j]
    # print(total)
    # total = 0
# arr = [
#     [3, 11, 2, 42],
#     [13, 112, 11, 412],
#     [311, 121, 111, 4112]
# ]   
# max=0
# min=9999
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]>max:
#             max=arr[i][j]
#         if  arr[i][j]<min:
#             min=arr[i][j]
#         # else:
# #         #     print("the number is equal")
# # print("the largest number is",max)
# # print("the smallest number is ",min)            
# arr = [
#      [3, 11, 2, 42],
#      [13, 112, 11, 412],
#      [311, 121, 111, 4112]
#  ]
# for i in range(len(arr)):
#     max=0
#     min=9999
#     for j in range(len(arr[i])):
#         if arr[i][j]>max:
#           max=arr[i][j]
#         if arr[i][j]<min:
#             min=arr[i][j]
#     print("the largest number is",max)
#     print("the smallest number is ",min)             

