def BinarySearch(arr, val):
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        mid = l + (r - l) / 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1

def add(x, y):
    ans = x + y
    return ans

val = add(10, 15)
if val > 30:
    print("ok")
else:
    print(val)    