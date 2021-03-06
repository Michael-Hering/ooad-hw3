class Rental:

	def __init__(self, toolslist, startDay, nights):
		self.__toolsList = []
		for tool in toolslist:
			self.__toolsList.append([tool, nights])
		self.__startDay = startDay
		self.__nightsRented = nights
		amt = 0
		for tool, n in self.__toolsList:
			amt += tool.getPricePerDay()*nights
		self.__totalAmount = amt
		

	def updateRental(self, toolsRequested, nightsRemaining):

		#Add a new tool to the rental, discard repeat tools they already have
		amt = 0
		for t in toolsRequested:
			if t not in self.__toolsList:
				self.__toolsList.append([t, nightsRemaining])
				amt += t.getPricePerDay()*nightsRemaining
		self.__totalAmount += amt

	def getStartDay(self):
		return self.__startDay

	def getNightsRented(self):
		return self.__nightsRented

	def getToolsList(self):
		return self.__toolsList

	def getAmount(self):
		return self.__totalAmount





		
		
