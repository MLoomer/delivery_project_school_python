from HashTable import HashTable

class Truck:
    def __init__(self, capacity):
        self.capacity = capacity
        self.packages = HashTable(capacity)
        self.address = "0"
        self.package_IDs = []
        self.distance = 0.0
        self.map = []
        self.mapIndex = []

    def loadPackage(self, package):
        packageID, *packageValues = package
        self.packages.insert(packageID, packageValues)
        self.package_IDs.append(packageID)

    def removePackage(self, package):
        print(f"Removing package {package}")
        packageID, *packageValues = package
        self.packages.remove(package)
        self.package_IDs.remove(packageID)

    def add_to_Map(self, address, full_map):
        add_check = None
        for index, row in enumerate(full_map):
            if address in row[0]:
                self.map.append(row)
                return index
        if add_check is None: print(f"No Match for address {address}")

    def condenseMap(self):
        filtered_data = []
        for row in self.map:
            filtered_row = [row[i] for i in self.mapIndex]
            filtered_data.append(filtered_row)
        print("this")
        print(filtered_data)

            #get address
            #match to top, collect index
            #at the end delete all cols that dont have matching index
