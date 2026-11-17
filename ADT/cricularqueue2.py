# Circular queue with current size
"""
- Front pointer -> points to the starting value
- rear pointer -> points to the ending value / next empty space
- current size -> used to track how many values are present
"""
# MJ 23 / Q2
class SaleData:
    def __init__(self, id, q):
        self.id = id
        self.quantity = q
        
CircularQueue = [SaleData("", -1) for i in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(record):
    global CircularQueue, Head, Tail, NumberOfItems
    size = len(CircularQueue)
    if NumberOfItems == size:
        return -1
    
    CircularQueue[Tail] = record
    Tail = (Tail + 1) % size
    NumberOfItems += 1
    return 1

def Dequeue():
    global CircularQueue, Head, Tail, NumberOfItems
    size = len(CircularQueue)
    if NumberOfItems==0:
        return SaleData("", -1) # return empty record
    temp=CircularQueue[Head]
    CircularQueue[Head]=SaleData("", -1)
    Head=(Head+1)%size
    return temp
    
def EnterRecord():
    id = input("Enter ID: ")
    q = int(input("Enter quantity: "))
    record = SaleData(id, q)
    res = Enqueue(record)
    if res == -1:
        print("Full")
    else:
        print("Stored") 
for i in range(6):
    newval=EnterRecord()
RECORD=Dequeue() 
print("the dequeued value is",RECORD.id)        
           
        
    
        
    
    
    

    
            