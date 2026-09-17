"""
Revising all previous chapters with OOP
class -> Algorithms 
Attributes -> array
Functions -> searching, sorting
"""

class Algorithms:
    def __init__(self, arr):
        self.__arr = list(arr)
        
    def setArr(self, newArr):
        self.__arr = list(newArr) 
    
    def getArr(self):
        return self.__arr
    
    def linearSearch(self, val):
        for i in range(len(self.__arr)):
            if self.__arr[i] == val:
                return i
        
        return -1
    
    def binarySearch(self, val):
        l = 0
        r = len(self.__arr) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if self.__arr[mid] == val:
                return mid
            elif self.__arr[mid] > val:
                r = mid - 1
            elif self.__arr[mid] < val:
                l = mid + 1    
    
        return -1
    
    def bubbleSort(self):
        lb = 0
        ub = len(self.__arr) - 1
        swap = True
        while swap and ub >= 1:
            swap = False
            for i in range(ub):
                if self.__arr[i] > self.__arr[i + 1]:
                    swap = True
                    temp = self.__arr[i]
                    self.__arr[i] = self.__arr[i + 1]
                    self.__arr[i + 1] = temp
            ub -= 1
    
    def bubbleSortDesc(self):
            lb = 0
            ub = len(self.__arr) - 1
            swap = True
            while swap and ub >= 1:
                swap = False
                for i in range(ub):
                    if self.__arr[i] < self.__arr[i + 1]:
                        swap = True
                        temp = self.__arr[i]
                        self.__arr[i] = self.__arr[i + 1]
                        self.__arr[i + 1] = temp
                ub -= 1
    
    def insertionSort(self):
        for i in range(1, len(self.__arr)):
            key = self.__arr[i]
            place = i
            while place > 0 and key < self.__arr[place - 1]:
                self.__arr[place] = self.__arr[place - 1]
                place -= 1
            
            self.__arr[place] = key    
        
        
    def insertionSortDesc(self):
        for i in range(1, len(self.__arr)):
                    key = self.__arr[i]
                    place = i
                    while place > 0 and key > self.__arr[place - 1]:
                        self.__arr[place] = self.__arr[place - 1]
                        place -= 1
                    
                    self.__arr[place] = key
    
a1 = Algorithms([2,3,4])
# print(a1.getArr())
idx = a1.linearSearch(90)
print(idx)    

a1.setArr([1,2,3,4,5,6,7,10])
idx = a1.binarySearch(11)
print(idx)
           
a2 = Algorithms([23,11,21,5,2,4,1])
a2.bubbleSort()
print(a2.getArr())           
a2.bubbleSortDesc()
print(a2.getArr())           
a2.insertionSort()
print(a2.getArr())           
a2.insertionSortDesc()
print(a2.getArr())           
    
a3 = Algorithms(["apple", "banana", "peach"])  
a3.bubbleSort()
print(a3.getArr())           
a3.bubbleSortDesc()
print(a3.getArr())           
a3.insertionSortDesc()
print(a3.getArr())   
a3.insertionSort()
print(a3.getArr())           
idx = a3.binarySearch("peach")
print(idx)
idx = a3.binarySearch("peach3e23")
print(idx)