
class TruckService:
    def __init__(self, truck, map):
        self.truck = truck
        self.map = map
        self.rowOffset, self.colOffset, self.valuemap = self.remove_labels()

    def get_remaining_id_addresses(self):
        remaining_addresses = []
        for id in self.truck.package_IDs:
            addr = self.truck.packages.lookup(id)[0]
            remaining_addresses.append([id, addr])
        return remaining_addresses

    def get_remaining_addresses(self, remaining_addresses):
        arr = []
        for address in remaining_addresses:
            arr.append(address[1])
        return arr

    def remove_labels(self):
        arr = []
        rowOffset = 1
        value_map = self.map.copy()
        colOffset = 2
        for i in range(len(value_map)):
            if (i > 0):
                arr.append(value_map[i][colOffset:])
        return rowOffset, colOffset, arr

    def get_matching_ids(self, address, id_address):
        arr = []
        for row in id_address:
            if address in row[1]:
                arr.append(row[0])
        return arr

    def deliver_a_package(self):
        current_address = self.truck.address
        id_address = self.get_remaining_id_addresses()
        remaining_addresses = self.get_remaining_addresses(id_address)
        address_to_go, distance = self.nearest_drive_alg(current_address, remaining_addresses)
        self.truck.address = address_to_go
        self.truck.distance += float(distance)
        print(f"delivered to {self.truck.address}, distance is {self.truck.distance}")
        self.truck.removePackages(self.get_matching_ids(self.truck.address, id_address))
        if (len(self.truck.package_IDs) == 0): return True

    def get_address(self, index, travel_map):
        return travel_map[0][index]

    def get_row_index(self, value, arr):
        for i, row in enumerate(arr):
            if value in row[0]:
                return i - 1

    def getXYValue(self, rowInd, i, valuemap):
        # print(f"rowInd {rowInd}, i = {i}")
        # print(f"travelmap: {valuemap[rowInd]}")
        if valuemap[rowInd][i] == "":
            return valuemap[i][rowInd]
        return valuemap[rowInd][i]

    def nearest_drive_alg(self, current_address, remaining_addresses):
        rowInd = self.get_row_index(current_address, self.map)
        min = 9999
        index = 9999
        for i in range(len(self.valuemap[rowInd])):
            value = float(self.getXYValue(rowInd, i, self.valuemap))
            if (value < min) and (rowInd != i):
                addrr = self.get_address(i + self.colOffset, self.map).split("\n")[1].lstrip()
                if addrr in remaining_addresses:
                    min = value
                    index = i
        if (index == 9999): print("failed to find match")
        new_address = self.get_address(index + self.colOffset, self.map).split("\n")[1].lstrip()
        return new_address, min

class DeliveryService:
    def __init__(self, trucks, map):
        self.trucks = trucks
        self.map = map


    def deliverPackages(self):

        for truck in self.trucks:
            delivery = TruckService(truck, self.map)
            empty = delivery.deliver_a_package()
            if empty is True:
                print(f"Truck completed trip, total distance: {truck.distance}")
                self.trucks.remove(truck)
        # while trucks are not empty
        if self.trucks:
            self.deliverPackages()
        else:
            return None



