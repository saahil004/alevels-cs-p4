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
        
# outputNodes(LinkedList, startPointer)        
        
# adds to the end of the linkedlist    
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


def AddToStart(val):
    global LinkedList, startPointer, emptyList
    
    if emptyList == -1:
        return False
    
    curr = emptyList
    LinkedList[curr].data = val
    emptyList = LinkedList[emptyList].nextNode
    
    LinkedList[curr].nextNode = startPointer
    startPointer = curr
    return True


# print("Before")
# outputNodes(LinkedList, startPointer)
# res = addNode(LinkedList)
# if res == True:
#     print("Added")
# else:
#     print("Not added")    
# print("After")
# res = addNode(LinkedList)
# if res == True:
#     print("Added")
# else:
#     print("Not added")    
# print("After")
# res = addNode(LinkedList)
# if res == True:
#     print("Added")
# else:
#     print("Not added")    
# print("After")
# res = addNode(LinkedList)
# if res == True:
#     print("Added")
# else:
#     print("Not added")    
# print("After")
# res = addNode(LinkedList)
# if res == True:
#     print("Added")
# else:
#     print("Not added")    
# print("After")
# outputNodes(LinkedList, startPointer)      

print("Before:")
outputNodes(LinkedList, startPointer)
res = AddToStart(200)
if res == True:
    print("Added")
else:
    print("Not added")
print("After:")
res = AddToStart(300)
if res == True:
    print("Added")
else:
    print("Not added")
print("After:")
res = AddToStart(500)
if res == True:
    print("Added")
else:
    print("Not added")
print("After:")
outputNodes(LinkedList, startPointer)
        