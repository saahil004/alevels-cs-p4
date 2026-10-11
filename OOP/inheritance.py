# Only use protected attributes in inheritance
# protected can be only accessed in parent and child


class Employee:
    def __init__(self, id, name, salary):
        self._id = id
        self._name = name
        self._salary = salary
    
    def getName(self):
        return self._name        
        
# two types of employees
""""
- Part time -> id, name, salary, overtimeBonus
- Full time -> id, name, salary, bonus
"""            

class PTEmployee(Employee):
    def __init__(self, id, name, sal, otb):
            super().__init__(id, name, sal)
            self.__overtimeBonus = otb




class FTEmployee(Employee):
    def __init__(self, id, name, sal, b):
        super().__init__(id, name, sal)
        self.__bonus = b
    



pte = PTEmployee(1, "Saahil", 2000, 10)
print(pte.getName())