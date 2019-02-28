import random

class Customer:
    def __init__(self, name):
        self.name = name
        self.toolsRented = []

    def pickTool(tools):
        return random.choice(tools)
    
    def rentTool(tool):
        self.toolsRented.append(tool)
    
    def returnTool(tool):
        self.toolsRented.remove(tool)
        return tool
    
    def getNumberToolsRented():
        return min(random.randint(self.minTools, self.maxTools), 3-len(toolsRented))
    
    def getDaysRented():
        return random.randint(self.minDays, self.maxDays)

    # Customer randomly shows up with 50% chance if store has enough tools,
    # or 0% chance if store doesn't have enough tools
    def isComing(numAvailable):
        return numAvailable >= self.minTools and random.random() > 0.5
    
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