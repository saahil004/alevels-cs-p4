# Writing to a text file
"""
- Create a new file
- If a file exists -> overwrite
- writes from the top
----------------
functions:
file = open("name", "mode(w)")
file.write("hello\n")
\n -> any future writes are done from next line, 
moves end of file to next line
"""

# Appending to a text file
"""
- writes from the end of file
"""
""""""""""""""""""""""""""""""""""""



# creating a file
# file = open("writing.txt", "w")
# file.write("Hello\n")
# file.write("World\n")
# file.close()

# appending to a file
# names = ["ali", "zain", "abbas"]
# file = open("writing.txt", "a")
# for i in range(len(names)):
#     file.write(names[i] + '\n')
# file.close()


# writing or appending an object
# cars.txt -> car objects, model, year, horsepower
class Car:
    def __init__(self, m, y, hp):
        self.__model = m
        self.__year = y
        self.__horsepower = hp
    
    def GetModel(self):
        return self.__model
        
    def GetYear(self):
        return self.__year    
    
    def GetHP(self):
        return self.__horsepower    

"""
city
2001
200
corolla
2014
300
"""
# cars = [Car("city", "2001", 200), Car("corolla", "2014", 300), Car("civic", "2012", 250)]
# file = open("cars.txt", "a")
# for i in range(len(cars)):
#     file.write(cars[i].GetModel() + "\n")
#     file.write(cars[i].GetYear() + '\n')
#     file.write(str(cars[i].GetHP()) + '\n')
# file.close()    
    