class Tool:
    def getName(self):
        return self.name
    
    def getPricePerDay(self):
        return self.pricePerDay
    
    # for debug purposes, so we can print them out and see what they are
    def __repr__(self):
        return type(self).__name__ + "('" + self.name.replace("'","\\'") + "')"

class PaintingTool(Tool):
    def __init__(self, name):
        self.name = name
        self.pricePerDay = 5.00

class ConcreteTool(Tool):
    def __init__(self, name):
        self.name = name
        self.pricePerDay = 15.00

class PlumbingTool(Tool):
    def __init__(self, name):
        self.name = name
        self.pricePerDay = 10.00

class WoodworkTool(Tool):
    def __init__(self, name):
        self.name = name
        self.pricePerDay = 20.00

class YardworkTool(Tool):
    def __init__(self, name):
        self.name = name
        self.pricePerDay = 7.50