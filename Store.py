class Store:

	def __init__(self, inv):
		self.__activeRentals = {}
		self.__rentalHistory = []
		self.__inventory = inv
		self.__numberOfTools = len(inv)
		self.__balance = 0

	def newRental(self, customer, toolsRequested, nightsRequested):

		if customer in self.__activeRentals.keys();
			rental = self.__activeRentals[customer]
			rental.updateRental(toolsRequested, nightsRequested)

		else:
			rental = Rental(toolsRequested, nightsRequested)
			
		self.__activeRentals[customer] = rental

	def getNumberOfTools(self):
		return len(inv)