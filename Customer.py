import random

class Customer:
    def __init__(self, name):
        self.__name = name
        self.__toolsRented = []
    
    def getName(self):
        return self.__name

    def pickTool(self, tools):
        return random.choice(tools)
    
    def rentTool(self, tool, nights):
        self.__toolsRented.append([tool, nights])
    
    def manageRentedTools(self):
        for pair in self.__toolsRented:
            if pair[1] == 0:
                self.__toolsRented.remove(pair)
            else:
                pair[1] -= 1
    
    def getNumberToolsRented(self):
        return min(random.randint(self._minTools, self._maxTools), 3-len(self.__toolsRented))
    
    def getDaysRented(self):
        return random.randint(self._minDays, self._maxDays)

    # Customer randomly shows up with 50% chance if store has enough tools,
    # or 0% chance if store doesn't have enough tools
    def isComing(self, numAvailable):
        return numAvailable >= self._minTools and len(self.__toolsRented) < 3 and random.random() > 0.5
    
    # for debug purposes, so we can print them out and see what they are
    def __repr__(self):
        return self.__name

class CasualCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self._minTools = 1
        self._maxTools = 2
        self._minDays = 1
        self._maxDays = 2

class BusinessCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self._minTools = 3
        self._maxTools = 3
        self._minDays = 7
        self._maxDays = 7

class RegularCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self._minTools = 1
        self._maxTools = 3
        self._minDays = 3
        self._maxDays = 5