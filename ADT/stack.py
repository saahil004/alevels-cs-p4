# Stack

# Arrays are passed by reference in python
# normal variable always go by val

# def stackFull(top, size):
#     if top == size:
#         return True
#     return False

# def stackEmpty(top):
#     if top == 0:
#         return True
#     return False

# def push(val, stack, t, s):
#     if stackFull(t, s) == True:
#         return t # stack overflow
#     stack[t] = val
#     t += 1
#     return t

# def pop(stack, top):
#     if stackEmpty(top) == True:
#         return top
    
#     top = top - 1
#     stack[top] = None
#     return top

# def valAtTop(stack, top):
#     if top == 0:
#         return -1
#     return stack[top - 1]


# stack = [None for i in range(5)] # stack of size 5
# top = 0 # points to next empty position
# size = 5

# top = push(12, stack, top, size)    
# top = push(13, stack, top, size)    
# top = push(14, stack, top, size)    
# print(stack)

# top = pop(stack, top)
# top = pop(stack, top)
# print(stack)

global StackPointer
global StackData
StackPointer = 0
StackData = [None for i in range(10)]

def PrintStack():
    global StackPointer, StackData
    for i in range(StackPointer):
        print(StackData[i])
    
    print("Stack Pointer: ", StackPointer)

PrintStack()        
    