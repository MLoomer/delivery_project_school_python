from HashTable import HashTable
import datetime

#Truck Object
class Truck:
    def __init__(self, name, capacity, depart_time, status, ids):
        self.name = name
        self.capacity = capacity
        self.packages = HashTable(capacity)
        self.address = "4001 South 700 East"
        self.package_IDs = []
        self.distance = 0.0
        self.time = depart_time
        self.status = status
        self.ids = ids

    #Never used
    def __str__(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, Distance: {self.distance}, time {self.time}\n"

    #package adder
    def loadPackage(self, package):
        self.packages.insert(int(package.ID), package)
        self.package_IDs.append(int(package.ID))

    #package remover (only by id list, still listed within truck
    def removePackage(self, id, time):
        status = f"DELIVERED"
        self.update_package(id, status, time)
        self.package_IDs.remove(id)

    #allows for loop removal
    def removePackages(self, ids, time):
        for id in ids:
            self.removePackage(id, time)

    #allows for loop updating package status
    def update_packages(self, status):
        for id in self.package_IDs:
            self.update_package(id, status, None)

    #update package status
    def update_package(self, id, status, time):
        package = self.packages.lookup(id)
        if time:
            package.delivery_time = time
        package.status = status
