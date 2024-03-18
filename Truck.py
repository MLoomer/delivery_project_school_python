from HashTable import HashTable

class Truck:
    def __init__(self, capacity):
        self.capacity = capacity
        self.packages = HashTable(capacity)
        self.address = "Hub"

    def loadPackage(self, package):
        packageID, *packageValues = package
        self.packages.insert(packageID, packageValues)

    def removePackage(self, package):
        packageID, *packageValues = package
        self.packages.remove(packageID)