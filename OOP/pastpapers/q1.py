# class Vehicle:
#     # PRIVATE ID : STRING
#     # PRIVATE MaxSpeed : INTEGER
#     # PRIVATE CurrentSpeed : INTEGER
#     # PRIVATE IncreaseAmount : INTEGER
#     # PRIVATE HorizontalPosition : INTEGER
    
#     def __init__(self, id, ms, ia):
#         self.__ID = id
#         self.__MaxSpeed = ms
#         self.__CurrentSpeed = 0
#         self.__IncreaseAmount = ia
#         self.__HorizontalPosition = 0
        
#     def GetCurrentSpeed(self):
#         return self.__CurrentSpeed
     
#     def GetIncreaseAmount(self):
#         return self.__IncreaseAmount
     
#     def GetMaxSpeed(self):
#         return self.__MaxSpeed
     
#     def GetHorizontalPosition(self):
#         return self.__HorizontalPosition
    
#     def SetCurrentSpeed(self, cs):
#         self.__CurrentSpeed = cs
    
#     def SetHorizontalPosition(self, cs):
#         self.__HorizontalPosition = cs
        
#     def IncreaseSpeed(self):
#         self.__CurrentSpeed += self.__IncreaseAmount  
#         if self.__CurrentSpeed > self.__MaxSpeed:
#             self.__CurrentSpeed = self.__MaxSpeed 
#         self.__HorizontalPosition += self.__CurrentSpeed 
        
#     def OutputPositions(self):
#         print("Horizontal Position: ", self.__HorizontalPosition)   
#         print("Current Speed: ", self.__CurrentSpeed)
         
     
# class Helicopter(Vehicle):
#     # PRIVATE VerticlePosition : INTEGER
#     # PRIVATE VerticleChange : INTEGER
#     # PRIVATE MaxHeight : INTEGER
    
#     def __init__(self, id, ms, ia, vc, mh):
#         super().__init__(id, ms, ia)
#         self.__VerticalPosition = 0
#         self.__VerticalChange = vc
#         self.__MaxHeight = mh

#     def IncreaseSpeed(self):
#         self.__VerticalPosition += self.__VerticalChange
#         if self.__VerticalPosition > self.__MaxHeight:
#             self.__VerticalPosition = self.__MaxHeight
        
#         super().SetCurrentSpeed(super().GetCurrentSpeed() + super().GetIncreaseAmount())
#         if super().GetCurrentSpeed() > super().GetMaxSpeed():
#             super().SetCurrentSpeed(super().GetMaxSpeed())
#         super().SetHorizontalPosition(super().GetHorizontalPosition() + super().GetCurrentSpeed())
        
#     def OutputPositions(self):
#             super().OutputPositions()
#             print("Vertical Position: ", self.__VerticalPosition)



# car = Vehicle("Tiger", 100, 20)  
# helicopter = Helicopter("Lion", 350, 40, 3, 100)
# car.IncreaseSpeed()              
# car.IncreaseSpeed()
# car.OutputPositions()              
# helicopter.IncreaseSpeed()              
# helicopter.IncreaseSpeed()
# helicopter.OutputPositions()              






class Character:
    # PRIVATE Name : STRING
    # PRIVATE XPosition : INTEGER
    # PRIVATE YPosition : INTEGER
    def __init__(self,Name,XPos,YPos):
        self.__Name = Name
        self.__XPosition = XPos
        self.__YPosition = YPos
    def GetXPosition(self):
        return self.__XPosition
    def GetYPosition(self):
        return self.__YPosition
    def SetXPosition(self,NewXPos):
        self.__XPosition += NewXPos
        if (self.__XPosition > 10000):
            self.__XPosition = 10000
        if (self.__XPosition < 0):
            self.__XPosition = 0
    def SetYPosition(self,NewYPos):
            self.__YPosition += NewYPos
            if (self.__YPosition > 10000):
                self.__YPosition = 10000
            if (self.__YPosition < 0):
                self.__YPosition = 0
    def Move(self,position):
        if (position == "up"):
            self.__YPosition += 10
        if (position == "down"):
            self.__YPosition -= 10
        if (position == "left"):
            self.__XPosition -= 10
        if (position == "right"):
            self.__XPosition += 10
            
Jack = Character("Jack",50,50)

class BikeCharacter(Character):
    def __init__(self,Name,XPos,YPos):
        super().__init__(Name,XPos,YPos)
    def Move(self,position):
        if (position == "up"):
            super().SetYPosition(20)
        if (position == "down"):
            super().SetYPosition(-20)
        if (position == "left"):
            super().SetXPosition(-20)
        if (position == "right"):
            super().SetXPosition(20)
            
Karla = BikeCharacter("Karla",100,50)
CharacterSelection = input("Which Character Would You Like To Move?")
DirectionSelection = input("Choose Which Direction To Move: ")
if (CharacterSelection == "Jack"):
    Jack.Move(DirectionSelection)
    print("Jack's new postion is X =", Jack.GetXPosition(), "Y =", Jack.GetYPosition())
elif (CharacterSelection == "Karla"):
    Karla.Move(DirectionSelection)
    print("Karla's new position is X =", Karla.GetXPosition(), "Y =", Karla.GetYPosition())
else:
    print("invalid name please try again")
    CharacterSelection = input("Which Character Would You Like To Move?")
    DirectionSelection = input("Choose Which Direction To Move: ")









