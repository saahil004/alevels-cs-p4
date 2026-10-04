class Stack:
    def __init__(self, size):
        self.__size = size
        self.__top = 0
        self.__arr = [None for i in range(size)]
        
    def push(self, val):
        if self.__top == self.__size:
            return False # stack overflow
        
        self.__arr[self.__top] = val
        self.__top += 1
        return True
    
    def pop(self):
        if self.__top != 0:
            return -1 # stack underflow
        
        val = self.__arr[self.__top - 1]
        self.__top -= 1
        return val
    
    def printStack(self):
        print("Stack with top pointer ", self.__top, ":")
        for i in range(self.__top):
            print(self.__arr[i])
    
s1 = Stack(10)
s1.push(11)        
s1.push(12)        
s1.push(13)
s1.printStack()        
s1.push(14)        
s1.push(15) 
s1.push(30)       
s1.printStack()
          
              
        
        