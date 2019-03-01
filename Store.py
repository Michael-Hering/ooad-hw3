from Rental import *

class Store:

	def __init__(self, inv):
		self.__activeRentals = {}
		self.__rentalHistory = []
		self.__inventory = inv
		self.__balance = 0

	def newRental(self, customer, toolsRequested, nightsRequested, currentDay):

		if customer in self.__activeRentals.keys():
			rental = self.__activeRentals[customer]

			#nights = nightsRequested - nights that have already passed
			nightsRemaining = nightsRequested - (currentDay - rental.getStartDay())

			#Check for past tools

			#Update inventory & balance
			for tool in toolsRequested:
				if tool not in rental.getToolsList():

					self.__balance += tool.getPricePerDay()*nightsRemaining

					for item in self.__inventory:
						if tool == item:
							self.__inventory.remove(item)

			#Update rental
			rental.updateRental(toolsRequested, nightsRemaining)


		else:
			
			#Update inventory & balance
			for t in toolsRequested:

				self.__balance += t.getPricePerDay()*nightsRequested


				for item in self.__inventory:
					if t == item:
						self.__inventory.remove(item)

			#Create rental
			rental = Rental(toolsRequested, currentDay, nightsRequested)

			
		self.__activeRentals[customer] = rental

	def inventoryReturns(self, currentDay):
		rentalsToRemove = []
		for customer in self.__activeRentals.keys():
			rental = self.__activeRentals[customer]
			expired = (rental.getNightsRented()) == (currentDay - rental.getStartDay())
			if expired:
				toolsReturned = rental.getToolsList()
				for t in toolsReturned:
					self.__inventory.append(t)

				rentalsToRemove.append(customer)


		#Delete rental and update history
		for cust in rentalsToRemove:
			rental = self.__activeRentals[cust]
			self.__rentalHistory.append([cust, rental.getToolsList(), rental.getAmount(), rental.getNightsRented()])

			del self.__activeRentals[cust]

	def getNumberOfTools(self):
		return len(self.__inventory)
	
	def getInventory(self):
		return self.__inventory

	def printReport(self):

		print("Number of tools currently in the store: %d\nInventory List: %s" %(self.getNumberOfTools(), self.__inventory))
		print("Amount of money that the store made: %d" %self.__balance)
		print("Completed Rentals: ")
		for cust, gt, amt, nights in self.__rentalHistory:
			print("Customer %s rented tools %s for %d nights at a cost of %d" % (cust, gt, nights, amt))
		print("Active rentals:")
		for customer in self.__activeRentals.keys():
			rental = self.__activeRentals[customer]
			gt, amt, nights = [rental.getToolsList(), rental.getAmount(), rental.getNightsRented()]
			print("Customer %s is currently renting tools %s for %d nights at a cost of %d" % (customer, gt, nights, amt))
