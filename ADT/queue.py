# Linear Queue

"""
Works on -> First in first out (FIFO)
Structure:
1) array -> actual queue
2) front pointer -> points to start value (stores start index)
3) rear pointer -> points to the last value or next empty position

Functions:
1) Enqueue -> adding a value to a queue
2) Dequeue -> removing a value from the queue
"""

queue = [None for i in range(5)]
fp = -1
rp = -1

def QueueFull():
    global queue, fp, rp
    if rp == len(queue) - 1:
        return True
    return False

def QueueEmpty():
    global queue, fp, rp
    if fp == -1 and rp == -1:
        return True
    return False

def Enqueue(val):
    global queue, fp, rp
    
    # Case 1: Queue full
    if QueueFull() == True:
        return False # Queue full so no enqueue
    
    # Case 2: Queue empty
    if QueueEmpty() == True:
        rp += 1
        fp += 1
        queue[fp] = val
        return True # Successful
    
    # Case 3: Queue not empty 
    rp += 1
    queue[rp] = val
    return True

def Dequeue():
    global queue, fp, rp
    if QueueEmpty() == True:
        return -1
    
    temp = queue[fp]
    queue[fp] = None
    fp += 1
    
    if fp > rp:
        rp = -1
        fp = - 1
    return temp


# print(queue)
# success = Enqueue(12)
# print("12 was enqueued? ", success)
# success = Enqueue(14)
# print("14 was enqueued? ", success)
# success = Enqueue(15)
# print("15 was enqueued? ", success)
# success = Enqueue(17)
# print("17 was enqueued? ", success)
# success = Enqueue(19)
# print("19 was enqueued? ", success)
# success = Enqueue(55)
# print("55 was enqueued? ", success)
# print(queue)
    
        
