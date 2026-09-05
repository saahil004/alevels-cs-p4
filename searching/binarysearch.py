# Binary searching
# Condition: Array must be sorted
"""
- l mid r
- mid position
- if number > mid position value -> left side discard left = mid + 1
- if number < mid position value -> right side discard right = mid - 1
- if number is at mid position -> value found
ending condition -> found or l > r
"""

# arr = [2, 4, 5, 6, 9, 11] # n = 6
# l = 0 # left index
# r = len(arr) - 1 # right index
# found = False # assume value is not found at start
# print(arr)
# num = int(input("Enter value to be found: "))
#
# while found == False and l <= r: # dono mein se ek bhi false hojaye tou binary search end
#     mid = int((l + r) / 2) # calculate mid index
#
#     if arr[mid] == num: # value found at mid
#         found = True
#     elif arr[mid] < num: # left side discard
#         l = mid + 1
#     elif arr[mid] > num: # right side discarded
#         r = mid - 1
#
# if found:
#     print("Value found.")
# else:
#     print("Value not found.")
#

# mid = l + (r - l) / 2

def binarySearch(arr, val):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = int(l + (r - l) / 2)
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            l = mid + 1
        else:
            r = mid - 1

    return -1

arr = [2, 3, 4, 5, 6, 8, 11, 13, 15]
print(arr)
val = int(input("Enter value to be found: "))
print("Index: ", binarySearch(arr, val))








