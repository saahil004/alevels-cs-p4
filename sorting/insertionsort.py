# insertion sort
"""
- start from second index
- assume left side is sorted
"""

def insertionSort(arr):
 for i in range(1, len(arr)):
    key = arr[i]
    place = i
    
    while place > 0 and arr[place - 1] > key: # arr[place - 1] < key in descending
        arr[place] = arr[place - 1]
        place -= 1
        
    arr[place] = key    
    
    

arr = [1, 7, 13, 8, 6]    
print("Before sorting: ", arr)
    
insertionSort(arr)  
print("After sorting: ", arr)
    