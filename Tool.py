class Tool:
    def getName(self):
        return self.__name
    
    def getPricePerDay(self):
        return self.__pricePerDay
    
    # for debug purposes, so we can print them out and see what they are
    def __repr__(self):
        return type(self).__name__ + "('" + self.__name.replace("'","\\'") + "')"

class PaintingTool(Tool):
    def __init__(self, name):
        self.__name = name
        self.__pricePerDay = 5.00

class ConcreteTool(Tool):
    def __init__(self, name):
        self.__name = name
        self.__pricePerDay = 15.00

class PlumbingTool(Tool):
    def __init__(self, name):
        self.__name = name
        self.__pricePerDay = 10.00

class WoodworkTool(Tool):
    def __init__(self, name):
        self.__name = name
        self.__pricePerDay = 20.00

class YardworkTool(Tool):
    def __init__(self, name):
        self.__name = name
        self.__pricePerDay = 7.50