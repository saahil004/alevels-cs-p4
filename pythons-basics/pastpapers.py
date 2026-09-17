# # DECLARE TheData : ARRAY[0 : 8] OF INTEGER
# TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

# def linearSearch():
#     num = int(input("Enter number: "))
#     for i in range(len(TheData)):
#         if TheData[i] == num:
#             print("Found")
#             return True
#     print("Not found")
#     return False

# ans1 = linearSearch()    
# ans2 = linearSearch()    


# Q)
"""
a) declare a 1d array of 10 elements -> 
2
23
54
13
3
5
64
11
22
33
[2 marks]
b) write a function for ascending order bubble sort [6 marks]
c) write a function for binary search -> takes array in which value needs to be searched
   and the target value, returns true if found, else false [6 marks]
d) sort ur array using ur function, then search 15 using binary search u wrote [2 marks]   
"""
#DECLARE arr:ARRAY[1:10]OF INTEGER
arr=[2,23,54,13,3,5,64,11,22,33]

def bubblesort(arr):
    ub=len(arr)-1
    swap=True
    while swap==True and ub>1:
        swap=False
        for j in range(0,ub):
            if arr[j]>arr[j+1]:
                swap=True
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        
        ub=-1        
print(arr)                


# Saturday 2 - 3 hours
"""
- python basics + practice + past papers
- functions
- binary searching
- string handling
"""