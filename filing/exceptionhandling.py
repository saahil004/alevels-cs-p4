# Exception Handling
"""
-> a way to handle errors ourselves
"""

"""
Syntax:
try:
    <code>
except Exception as e:
    <code if error occurs>    
"""

# arr = [2, 3, 4, 5]
# try:
#     print(arr[2])
# except Exception as e:
#     print("Error occurred: ", str(e))    

# Exception handling in filing
try:
    file = open("cars2.txt", "r")
    content = file.read()
    print(content)
    file.close()
except IOError as e:
    print("File error: ", str(e))