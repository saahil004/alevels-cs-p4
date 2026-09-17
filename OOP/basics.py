# Classes -> blueprints
# objects -> instance of that blueprint

"""
TYPE Car
    DECLARE model : STRING
    DECLARE engineType : STRING
    DECLARE company : STRING
    DECLARE auto : BOOLEAN
END TYPE

DECLARE myCar : Car
myCar.model <- "corolla"
myCar.engineType <- "1.8"
myCar.company <- "Toyota"
myCar.auto <- TRUE
"""

# too basic
# class Car:
#     model = ""
#     engine = ""
#     auto = False
    
# myCar = Car()
# myCar2 = Car()
# myCar.auto = True
# myCar.engine = "1.8"
# myCar.model = "corolla"
# print("Model of the car is: ", myCar.model)
    

# Constructors -> functions jo object bana ke dete hain
"""
- defined by def __init__(self): # self means the object itself
- constructor has the same name as class
- public
"""

"""
        Attributes
      |          |         |
     private   public   protected
private -> attributes cannot be accessed outside class
public -> can be accessed outside class just like record type
protected -> private for outside, accessible for children     
"""


# Attributes -> id, name, age, graduated
class Student:
    def __init__(self, id, name, age, grad):
        self.id = id
        self.name = name
        self.age = age
        self.graduated = grad
    
s1 = Student(1, "Ali", 20, True)
print("Student's name is: ", s1.name)



# Q) class of a book, a book must have an isbn number, a title, author
# make atleast 3 different objects of this class and all three of them must have a unique ISBN number


# Q: how do i access private attributes?
# in the class, using setters and getters


class BankAccount:
    def __init__(self, holder, bank, cardno, PIN):
        self.holder = holder
        self.bank = bank
        self.__cardno = cardno
        self.__pin = PIN
        
    def setCardNo(self, newNo):
        self.__cardno = newNo
    
    def setPin(self, newpin):
        self.__pin = newpin
    
    def getCardNo(self):
        return self.__cardno

    def getPin(self):
        return self.__pin

holder = input("Enter name of account holder: ")
bank = input("Enter the name of the bank: ")
card = input("Enter card number: ")
pin = input("Enter 4 digit pin: ")    
acc1 = BankAccount(holder, bank, card, pin)

# acc1.__pin = '1234' error

acc1.setPin("1234")

x = acc1.getCardNo()  
print("x is ", x)     
  
newpin = acc1.getPin()  
print("New pin was changed to: ", newpin)            


"""
Q) create a class named Employee 
with attributes -> id, name, type (parttime or fulltime), phone number
all attributes must be private
define setters and getters for all 
"""







    
