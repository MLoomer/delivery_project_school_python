from HashTable import HashTable
import datetime

class Truck:
    def __init__(self, name, capacity, depart_time):
        self.name = name
        self.capacity = capacity
        self.packages = HashTable(capacity)
        self.address = "4001 South 700 East"
        self.package_IDs = []
        self.distance = 0.0
        self.time = depart_time

    def __str__(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, Distance: {self.distance}, time {self.time}\n"

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