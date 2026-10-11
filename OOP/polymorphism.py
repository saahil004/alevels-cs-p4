# same thing, multiple forms

# class Animal:
#     def __init__(self, name):
#         self._name = name
        
#     def speak(self):
#         print("Animal is speaking")

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def speak(self): # override
#         super().speak()
#         print("Dog is barking")

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def speak(self):
#         print("Cat is meowing")    
            
# a = Animal("abc")
# a.speak()

# d = Dog("xyz")
# d.speak()   

# c = Cat("nfdjk")
# c.speak() 

class Shape:
    def __init__(self, l, b):
        self._length = l
        self._breadth = b
    
    def Area(self):
        print("Lets calculate area")
        
    def PrintDimensions(self):
        print("These are the dimensions")        
        
class Rectangle(Shape):
    def __init__(self, l, b):
        super().__init__(l, b)
    
    def Area(self):
        print("Area: ", self._length * self._breadth)
    
    def PrintDimensions(self):
        print("Rectangle: length=", self._length, " breadth=", self._breadth)

s = Shape(1, 2)
s.Area()

r = Rectangle(2, 4)
r.Area()                
                