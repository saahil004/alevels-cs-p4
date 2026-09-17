class Card:
    # __Number : INTEGER
    # __Colour : STRING
    
    def __init__(self, n, c):
        self.__Number = n
        self.__Colour = c
        
    def GetColour(self):
        return self.__Colour
        
    def GetNumber(self):    
        return self.__Number

cards = []
selected = [False for i in range(30)]
file = open(r"C:\Users\DELL\PycharmProjects\alevelcsp4\pastpapers\CardValues.txt", "r") # read mode
for i in range(30):  
    num = int(file.readline())
    colour = file.readline().strip('\n')
    c1 = Card(num, colour)
    cards.append(c1)
    
file.close()
for card in cards:
    print(card.GetColour())     

c = input("Enter colour to be found: ")
idx = -1
for i in range(30):
    if cards[i].GetColour() == c:
        idx = i
        break

if idx != -1:
    print("colour found", idx)        
    # print("colour found")        
else:
    print("colour not found")        
    
    
def ChooseCard(cards, selected):
    s = False
    while s == False:
     idx = int(input("Enter index (1 to 30) to select a card: "))
     if idx >= 1 and idx <= 30:
         idx -= 1
         if selected[idx] == False:
             return idx
    
         
    
    