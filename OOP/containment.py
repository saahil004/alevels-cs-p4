# Containment -> one class having an object of another class

class Engine:
    def __init__(self, hp):
        self.__horsepower = hp
    
    def setHP(self, newhp):
        self.__horsepower = newhp
    
    def getHP(self):
        return self.__horsepower
    
    def start(self):
        print("this engine started")
        
class Car:
      def __init__(self, m, horsep, seats):
          self.__model = m
          self.__engine = Engine(horsep)
          self.__seats = seats           
          
      def StartCar(self):
          print("open door")
          print("Starting start")
          self.__engine.start()

# c = Car("Honda city 2001", 200, 4)
# c.StartCar()                 

# Object array -> useful in filing etc
cars = [Car("", 0, 0) for i in range(500)]
cars[1].StartCar()