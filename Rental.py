class Rental:

	def __init__(self, toolslist, startDay, nights):
		self.__toolsList = toolslist
		self.__startDay = startDay
		self.__nightsRented = nights
		

	def updateRental(self, toolsRequested):

		#Add a new tool to the rental, discard repeat tools they already have
		for t in toolsRequested:
			if t not in toolslist:
				toolslist.append(t)

	def getStartDay(self):
		return self.__startDay

	def getNightsRented(self):
		return self.__nightsRented

	def getToolsList(self):
		return self.__toolsList





		
		
