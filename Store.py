class Store:

	def __init__(self, inv):
		self.__activeRentals = {}
		self.__rentalHistory = []
		self.__inventory = inv
		self.__numberOfTools = len(inv)
		self.__balance = 0

	def newRental(self, customer, toolsRequested, currentDay):

		nightsRequested = customer.getDaysRented()

		if customer in self.__activeRentals.keys():
			rental = self.__activeRentals[customer]

			#nights = nightsRequested - nights that have already passed
			nightsRemaining = nightsRequested - (currentDay - rental.startDay)

			#Check for past tools

			#Update inventory
			for tool in toolsRequested:
				if tool not in rental.getToolsList:
					for item in self.__inventory:
						if t == item:
							self.__inventory.remove(item)

			#Create rental
			rental.updateRental(toolsRequested, nightsRemaining)


		else:
			
			#Update inventory
			for t in toolsRequested:
				for item in self.__inventory:
					if t == item:
						self.__inventory.remove(item)

			#Create rental
			rental = Rental(toolsRequested, nightsRequested)

			
		self.__activeRentals[customer] = rental

	def reInventoryReturns(self):
		for customer in self.__activeRentals.keys():
			rental = self.__activeRentals[customer]
			expired = (rental.getNightsRented()) == (currentDay - rental.getStartDay())
			if expired:
				toolsReturned = rental.getToolsList()
				for t in toolsReturned:
					self.__inventory.append(t)

				del self.__activeRentals[customer]

	def getNumberOfTools(self):
		return len(inv)