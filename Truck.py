from HashTable import HashTable

class Truck:
    def __init__(self, capacity):
        self.capacity = capacity
        self.packages = HashTable(capacity)
        self.address = "4001 South 700 East"
        self.package_IDs = []
        self.distance = 0.0

    def loadPackage(self, package):
        packageID, *packageValues = package
        self.packages.insert(packageID, packageValues)
        self.package_IDs.append(packageID)

    def removePackage(self, id):
        self.packages.remove(id)
        self.package_IDs.remove(id)

    def removePackages(self, ids):
        for id in ids:
            self.removePackage(id)