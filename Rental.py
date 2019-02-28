class Rental:

	def __init__(self, toolslist, nights)
		self.__toolsList = toolslist
		self.__nightsRented = nights

	def updateRental(self, toolsRequested):

		#Add a new tool to the rental, discard repeat tools they already have
		for t in toolsRequested:
			if t not in toolslist:
				toolslist.append(t)




		
		
