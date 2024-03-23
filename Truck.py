from HashTable import HashTable
import datetime

class Truck:
    def __init__(self, name, capacity, depart_time, status):
        self.name = name
        self.capacity = capacity
        self.packages = HashTable(capacity)
        self.address = "4001 South 700 East"
        self.package_IDs = []
        self.distance = 0.0
        self.time = depart_time
        self.status = status

    def __str__(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, Distance: {self.distance}, time {self.time}\n"

    def loadPackage(self, package):
        self.packages.insert(int(package.ID), package)
        self.package_IDs.append(int(package.ID))

    def removePackage(self, id, time):
        status = f"DELIVERED AT {time}"
        self.update_package(id, status)
        self.package_IDs.remove(id)

    def removePackages(self, ids, time):
        for id in ids:
            self.removePackage(id, time)

    def update_packages(self, status):
        for id in self.package_IDs:
            self.update_package(id, status)

    def update_package(self, id, status):
        package = self.packages.lookup(id)
        package.status = status
