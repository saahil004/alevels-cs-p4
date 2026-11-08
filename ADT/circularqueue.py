# Circular Queue
"""
- Fixes wasted space issue by linear queue
- Uses circular increment: x = (x + 1) % size
- Full = rear ka next front ho. ((r + 1) % size == f) OR if u are using
 the currentSize approach then track queue size (currSize == size)
- Empty f and r == -1
"""

queue = [None for i in range(5)]
f = -1
r = -1

def CircularEnqueue(val):
    global queue, f, r
    size = len(queue)
    
    # Case 1: cannot enqueue, queue full
    if (r + 1) % size == f:
        return False
    
    # Case 2: Queue is empty
    if f == -1 and r == -1:
        f += 1
        r += 1
        queue[r] = val
        return True
    
    # Case 3: simple
    r = (r + 1) % size
    queue[r] = val
    return True

def CircularDequeue():
    global queue, f, r
    size = len(queue)
    
    # If empty, no dequeue
    if f == -1 and r == -1:
        return -1 
    
    temp = queue[f]
    queue[f] = None
    if f == r:
        f = -1
        r = -1
    else:    
        f = (f + 1) % size
    
    return temp    