import random

class Customer:
    def __init__(self, name):
        self.name = name
        self.toolsRented = []

    def getTool(tool):
        self.toolsRented.append(tool)
    
    def returnTool(tool):
        self.toolsRented.remove(tool)
        return tool
    
    def getNumberToolsRented():
        return random.randint(self.minTools, self.maxTools)
    
    def getDaysRented():
        return random.randint(self.minDays, self.maxDays)
    
    # for debug purposes, so we can print them out and see what they are
    def __repr__(self):
        return type(self).__name__ + "('" + self.name.replace("'","\\'") + "')"

class CasualCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.minTools = 1
        self.maxTools = 2
        self.minDays = 1
        self.maxDays = 2

class BusinessCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.minTools = 3
        self.maxTools = 3
        self.minDays = 7
        self.maxDays = 7

class RegularCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.minTools = 1
        self.maxTools = 3
        self.minDays = 3
        self.maxDays = 5