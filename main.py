from Tool import *
from Customer import *
from Rental import *
from Store import *

def readCatalog(filename):
    inventory = []
    with open(filename) as f:
        ToolCategory = PaintingTool
        for line in f:
            line = line.strip()
            if len(line) > 0:
                if line[0] == '[' and line[-1] == ']':
                    line = line[1:-1]
                    if line == "Painting":
                        ToolCategory = PaintingTool
                    elif line == "Concrete":
                        ToolCategory = ConcreteTool
                    elif line == "Plumbing":
                        ToolCategory = PlumbingTool
                    elif line == "Woodwork":
                        ToolCategory = WoodworkTool
                    elif line == "Yardwork":
                        ToolCategory = YardworkTool
                else:
                    inventory.append(ToolCategory(line))
    return inventory

def readCustomers(filename):
    customers = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                cust_lines = line.split()
                if len(cust_lines) > 1:
                    if cust_lines[1] == "Casual":
                        customers.append(CasualCustomer(cust_lines[0]))
                    elif cust_lines[1] == "Business":
                        customers.append(BusinessCustomer(cust_lines[0]))
                    else:
                        customers.append(RegularCustomer(cust_lines[0]))
    return customers

def main():
    inv = readCatalog("catalog.txt")

    store = Store(inv)
    
    customers = readCustomers("customers.txt")

    # for 35 night/day cycles
    for day in range(35):
        # First process all the returns (customer has already "returned" to store the EXPIRED rental)
        store.inventoryReturns(day)
        for customer in customers:
            customer.manageRentedTools()

        # Now rent tools to customers that come
        # This is a rough outline, may need to change based on implementation
        if store.getNumberOfTools() > 0:
            for customer in customers:
                if customer.isComing(store.getNumberOfTools()):
                    toolsRented = []
                    numberNights = customer.getDaysRented()
                    for i in range(customer.getNumberToolsRented()):
                        tool = customer.pickTool(store.getInventory())
                        toolsRented.append(tool)
                        customer.rentTool(tool, numberNights)
                    store.newRental(customer, toolsRented, numberNights, day)
        
    store.printReport()

if __name__ == "__main__":
    main()