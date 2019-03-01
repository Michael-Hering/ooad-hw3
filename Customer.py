import random

class Customer:
    def __init__(self, name):
        self.__name = name
        self.__toolsRented = []

    def pickTool(self, tools):
        return random.choice(tools)
    
    def rentTool(self, tool, days):
        self.__toolsRented.append([tool, days])
    
    def manageRentedTools(self):
        for pair in self.__toolsRented:
            if pair[1] == 0:
                self.__toolsRented.remove(pair)
            else:
                pair[1] -= 1
    # def returnTool(self, tool):
    #     self.__toolsRented.remove(tool)
    #     return tool
    
    def getNumberToolsRented(self):
        return min(random.randint(self.__minTools, self.__maxTools), 3-len(toolsRented))
    
    def getDaysRented(self):
        return random.randint(self.__minDays, self.__maxDays)

    # Customer randomly shows up with 50% chance if store has enough tools,
    # or 0% chance if store doesn't have enough tools
    def isComing(numAvailable):
        return numAvailable >= self.__minTools and len(self.__toolsRented) < 3 and random.random() > 0.5
    
    # for debug purposes, so we can print them out and see what they are
    def __repr__(self):
        return type(self).__name__ + "('" + self.__name.replace("'","\\'") + "')"

class CasualCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.__minTools = 1
        self.__maxTools = 2
        self.__minDays = 1
        self.__maxDays = 2

class BusinessCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.__minTools = 3
        self.__maxTools = 3
        self.__minDays = 7
        self.__maxDays = 7

class RegularCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.__minTools = 1
        self.__maxTools = 3
        self.__minDays = 3
        self.__maxDays = 5