class Node:
    # PUBLIC data : INTEGER
    # PUBLIC NextNode : INTEGER
    def __init__(self, d, n):
        self.data = d
        self.NextNode = n
LinkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6), Node(0, 8), Node(56, 3), Node(0, 9), Node(0, -1)]
startPointer = 0
emptyList = 5 
def outputNodes(linkedlist,startpointer):
    ptr=startpointer
    while ptr!=-1:
        print(linkedlist[ptr].data)
        ptr=linkedlist[ptr].NextNode
# outputNodes(LinkedList,startPointer)

def addNode(LinkedList):
    global startPointer,emptyList
    if emptyList==-1:
        return False
    val=int(input("enter your number"))
    curr = emptyList
    LinkedList[curr].data = val
    emptyList = LinkedList[emptyList].NextNode
    ptr=startPointer
    while LinkedList[ptr].NextNode!=-1:
        ptr = LinkedList[ptr].NextNode            
    LinkedList[ptr].NextNode = curr
    LinkedList[curr].NextNode = -1
    return True
print("before")
outputNodes(LinkedList,startPointer)
result=addNode(LinkedList)
if result==True:
    print("value added")
else:
    print("not added")
print("after")    
    
    
              


           