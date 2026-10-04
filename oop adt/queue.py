# Queue data structure
"""
- FIFO -> first in first out
- Linear Queue - wasted space
- Circular Queue - circular increment and utilizes wasted space

_______
front pointer -> points to the front of the queue
rear pointer -> end of the queue
"""
n = 5
queue = [None for i in range(n)]
fp = -1
rp = -1
# both pointers are -1 as queue is empty

def Enqueue(val):
    global n, queue, fp, rp
    if rp == n - 1:
        return False
    
    if fp == -1 and rp == -1:
        fp = 0
        rp = 0
        queue[rp] = val
        return True
    
    rp += 1
    queue[rp] = val
    return True

def Dequeue():
    global n, queue, fp, rp
    if fp == -1 and rp == -1:
        print("Queue empty")
        return -1
    
    temp = queue[fp]
    queue[fp] = None
    fp += 1
    print("Value dequeued: ", temp)
    if fp > rp:
        fp = -1
        rp = -1
        print("Queue is now empty.")
    return temp    
        
def printQueue():
    global fp, rp, n, queue
    print("Queue: ", end=" ")
    for i in range(fp, rp + 1):
        print(queue[i], end=" ")  
             
    print("\nFront pointer: ", fp)    
    print("Rear pointer: ", rp)    


print(Enqueue(1))
print(Enqueue(11))
print(Enqueue(12))
print(Enqueue(12))
print(Enqueue(12))
print(Enqueue(152))
printQueue()

Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
printQueue()

