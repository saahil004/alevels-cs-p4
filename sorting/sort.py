arr1=[1,6,3,4,5]
arr2=[5,4,3,2,1]

def bubblesort(arr):
    swap=True
    ub=len(arr)-1
    while swap==True and ub>=1:
        swap=False
        for i in range(ub):
             if arr[i]>arr[i+1]:
                 swap=True
                 temp=arr[i]
                 arr[i]=arr[i+1]
                 arr[i+1]=temp
    ub-=1
                 
            
    

def inbubble(arr):
    ub=len(arr)-1
    for i in range(ub+1):
        for j in range(ub):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                            
                   
 
bubblesort(arr1)
print(arr1)
 
inbubble(arr2)  
print (arr2)
                