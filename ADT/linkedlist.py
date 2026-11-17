# Linkedlist unordered (data is not sorted) question
# Node -> data + pointer to next node

class Node:
    # PUBLIC data : INTEGER
    # PUBLIC nextNode : INTEGER
    def __init__(self, d, n):
        self.data = d
        self.nextNode = n

LinkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6), Node(0, 8), Node(56, 3), Node(0, 9), Node(0, -1)]
startPointer = 0
emptyList = 5

def outputNodes(LinkedList, startPointer):
    ptr = startPointer
    while ptr != -1:
        print(LinkedList[ptr].data)
        ptr = LinkedList[ptr].nextNode
        
outputNodes(LinkedList, startPointer)        
        
        

# def insertAtEnd(Linkedlist, startPointer, val):
#     ptr = startPointer
#     while Linkedlist[ptr].NextNode != -1:
#         ptr = Linkedlist[ptr].NextNode
    
#     # now ptr stands at the last node
#     # add the new node in free position or append it in the list
#     new = Node(val, -1)
#     Linkedlist.append(new)
#     lastidx = len(Linkedlist) - 1
#     Linkedlist[ptr].NextNode = lastidx
    
# print("Before")    
# outputNodes(LinkedList, startPointer)
# insertAtEnd(LinkedList, startPointer, 100)
# print("After")
# outputNodes(LinkedList, startPointer)
    
    
def addNode(Linkedlist):
    global startPointer, emptyList
    if emptyList == -1:
        return False
    val = int(input("Enter value: "))
    
    curr = emptyList
    Linkedlist[curr].data = val
    emptyList = Linkedlist[emptyList].NextNode
    
    ptr = startPointer
    while Linkedlist[ptr].NextNode != -1:
        ptr = Linkedlist[ptr].NextNode
        
    Linkedlist[ptr].NextNode = curr
    Linkedlist[curr].NextNode = -1
    return True    

print("Before")
outputNodes(LinkedList, startPointer)
res = addNode(LinkedList)
if res == True:
    print("Added")
else:
    print("Not added")    
print("After")
res = addNode(LinkedList)
if res == True:
    print("Added")
else:
    print("Not added")    
print("After")
res = addNode(LinkedList)
if res == True:
    print("Added")
else:
    print("Not added")    
print("After")
res = addNode(LinkedList)
if res == True:
    print("Added")
else:
    print("Not added")    
print("After")
res = addNode(LinkedList)
if res == True:
    print("Added")
else:
    print("Not added")    
print("After")
outputNodes(LinkedList, startPointer)        
        