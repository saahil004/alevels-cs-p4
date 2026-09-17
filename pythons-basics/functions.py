# Functions
"""
- To group code that repeats again and again
- Functions -> returns a value
- Procedures -> do not return a value


-- return vs print
- return provides us a value
- print displays a value

n = len(arr) # returns length of an array arr

-- scope of a variable
- global variables -> can be used everywhere once defined
- local variables -> can only be used in a function where its defined

-- Parameters
- values that are to be used by function

FUNCTION FindItemPrice(ItemName : STRING) RETURN REAL

ENDFUNCTION

item <- "chips"
price <- FindItemPrice(item)

"""

# Syntax
"""
FUNCTION Add(x : INTEGER, y : INTEGER) RETURNS INTEGER
    <>
ENDFUNCTION


Python: - function and procedure are same
- no need to tell a return type
def <function name>(<parameter1>, <>, <>):
    <code>
    return <>
    
"""

def AddTwo(x, y):
    z = 0
    z = x + y
    return z

ans = AddTwo(5,11)
print("The value of answer is ", ans)
#
# num1 = 5
# num2 = 10
# print(num1 + num2)

"""
Q) make a function to take 3 integers that returns
 the largest of them all
"""

# array will be always passed by reference
# normal variables are always passed by value, python has no by reference