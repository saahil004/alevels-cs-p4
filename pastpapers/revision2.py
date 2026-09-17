class StringHandling:
    def __init__(self, s):
        self.__s = str(s)
        
    def stringToArr(self):
        s2 = self.__s
        return list(s2)
    
    def words(self):
        return self.__s.split(" ")
    
    def upperCase(self):
        return self.__s.upper()
    
    def lowerCase(self):
        return self.__s.lower()
    
    def concat(self, otherstr):
        self.__s += otherstr
        
    def setS(self, news):
        self.__s = news
    
    def getS(self):
        return self.__s
    
    def subString(self, start, end, stepidx):
        if start >= 0 and start < len(self.__s) and end < len(self.__s) and end >= 0 and start < end and stepidx > 0:
            return self.__s[start : end + 1 : stepidx]
        
        return None
    
    
s1 = StringHandling("i am studying computer science")
print(s1.upperCase())
s1.concat("...")
print(s1.getS())
words = s1.words()
print(words)
print(s1.subString(0, 10, 2))

arr = [None for i in range(10)]
numInt = 0

def appendNum(val, arr, count):
    
    if numInt < 10:
        arr[count] = val
        count += 1
        return count
    
    return count

numInt = appendNum(10, arr, numInt)
numInt = appendNum(5, arr, numInt)
print(arr, numInt)        
    
    