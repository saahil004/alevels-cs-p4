# bubble sort 
"""
- nested loop
- outer loop (for stopping conditions)
- inner loop (comparisions and swapping)
- swapping logic
- ub after each inner loop ub = ub - 1
- initialize swap to false after each iteration
"""

def inefficient(arr):
    ub = len(arr) - 1
    for i in range(ub + 1):
        for j in range(ub):
            if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
            


def bubbleSort(arr):
    ub = len(arr) - 1
    swap = True # assuming array is not sorted

    while swap == True and ub >= 1:
        swap = False
    
        for i in range(ub):
            if arr[i] > arr[i + 1]:
                swap = True
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
 
        ub -= 1 



arr = [5, 3, 2, 11, 9, 10]
arr2 = [43,12,1223,21,324,213,121,89,91]
inefficient(arr)
print(arr)

inefficient(arr2)
print(arr2)