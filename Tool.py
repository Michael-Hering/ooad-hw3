class Tool:
    def getName(self):
        return self._name
    
    def getPricePerDay(self):
        return self._pricePerDay
    
    def __repr__(self):
        return self._name

class PaintingTool(Tool):
    def __init__(self, name):
        self._name = name
        self._pricePerDay = 5.00

class ConcreteTool(Tool):
    def __init__(self, name):
        self._name = name
        self._pricePerDay = 15.00

class PlumbingTool(Tool):
    def __init__(self, name):
        self._name = name
        self._pricePerDay = 10.00

class WoodworkTool(Tool):
    def __init__(self, name):
        self._name = name
        self._pricePerDay = 20.00

class YardworkTool(Tool):
    def __init__(self, name):
        self._name = name
        self._pricePerDay = 7.50