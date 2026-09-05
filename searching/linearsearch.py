# value exists in array or not
# arr = [4, 2, 5, 6, 11]
# val = int(input("Enter value to be found: "))
# f = False
# for i in range(len(arr)):
#     if arr[i] == val:
#         f = True
#         break # loop exits
# if f == True:
#     print("Value found.")
# else:
#     print("Value not found.")
#

#
# arr = [21, 2, 4, 53, 23, 44]
# print(arr)
# num = int(input("Enter a number to be found: "))
# idx = -1
# for i in range(len(arr)):
#     if num == arr[i]:
#         idx = i
#         break
#
# if idx == -1:
#     print("Value not found")
# else:
#     print("Value found at: ", idx)


# def linear_search()
# def LinearSearch()
def linearSearch(arr, val): # return index of found value else return -1
    for i in range(len(arr)):
        if arr[i] == val:
            return i

    return -1

a = [12, 23, 2, 43, 42, 122, 42]
print(a)
val = int(input("Enter a value to be found: "))
index = linearSearch(a, val)
print("Value found at index: ", index)




