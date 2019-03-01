class Rental:

	def __init__(self, toolslist, startDay, nights)
		self.__toolsList = toolslist
		self.__startDay = startDay
		self.__nightsRented = nights
		

	def updateRental(self, toolsRequested):

		#Add a new tool to the rental, discard repeat tools they already have
		for t in toolsRequested:
			if t not in toolslist:
				toolslist.append(t)

	def getStartDay():
		return self.__startDay

	def getNightsRented():
		return self.__nightsRented

	def getToolsList():
		return self.__toolsList





		
		
