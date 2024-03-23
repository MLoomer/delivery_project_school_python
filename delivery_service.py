import datetime


class ValueService:
    def __init__(self):
        self.values = []

    def get_matching_ids(self, match, array):
        arr = []
        for row in array:
            if match in row[1]:
                arr.append(row[0])
        return arr

    def get_address(self, index, arr):
        return arr[0][index].split("\n")[1].lstrip()

    def get_row_index(self, value, arr):
        for i, row in enumerate(arr):
            if value in row[0]:
                return i - 1

    def getXYValue(self, i, j, arr):
        if arr[i][j] == "":
            return arr[j][i]
        return arr[i][j]

    def formatTime(self, time):
        hour, min = time.split(":")
        return [int(hour), int(min)]


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

    def remove_labels(self):
        arr = []
        rowOffset = 1
        value_map = self.map.copy()
        colOffset = 2
        for i in range(len(value_map)):
            if (i > 0):
                arr.append(value_map[i][colOffset:])
        return rowOffset, colOffset, arr

    def get_remaining_addresses(self, remaining_addresses):
        arr = []
        for address in remaining_addresses:
            arr.append(address[1])
        return arr

    def deliver_a_package(self):
        data = ValueService()
        current_address = self.truck.address
        id_address = self.get_remaining_id_addresses()
        remaining_addresses = self.get_remaining_addresses(id_address)
        address_to_go, distance = self.nearest_drive_alg(current_address, remaining_addresses)
        self.truck.address = address_to_go
        self.truck.distance = round(float(distance) + self.truck.distance, 2)
        self.truck.time += datetime.timedelta(hours=distance / 18)

        ids = data.get_matching_ids(self.truck.address, id_address)
        self.truck.removePackages(ids)
        print(f"Truck {self.truck.name} delivered package(s) {ids} to {self.truck.address}, traveled {float(distance)}, distance is {self.truck.distance}, time is {self.truck.time}")
        if (len(self.truck.package_IDs) == 0): return True

    def nearest_drive_alg(self, current_address, remaining_addresses):
        data = ValueService()
        rowInd = data.get_row_index(current_address, self.map)
        min = float('inf')
        index = None

        for i in range(len(self.valuemap[rowInd])):
            value = float(data.getXYValue(rowInd, i, self.valuemap))
            if (value < min) and (rowInd != i):
                address = data.get_address(i + self.colOffset, self.map)
                if address in remaining_addresses:
                    min = value
                    index = i

        if (index is None): print("failed to find match")
        new_address = data.get_address(index + self.colOffset, self.map)
        return new_address, min


class DeliveryService:
    def __init__(self, trucks, map, start_time_hours, update, stoptime):
        self.trucks = trucks
        self.pending_trucks = self.driver_limit()
        self.map = map
        self.delivered_trucks = []
        self.current_time = datetime.timedelta(hours=start_time_hours)
        self.update_data = update
        self.update_status = ""
        data = ValueService()
        hour, min = data.formatTime(stoptime)
        self.stop_time = datetime.timedelta(hours=hour, minutes=min)

    def driver_limit(self):
        arr = []
        for truck in self.trucks:
            if truck.name == "3":
                self.trucks.remove(truck)
                arr.append(truck)
        return arr

    def deliverPackages(self):
        while len(self.trucks):
            for truck in self.trucks:
                if (truck.time <= self.current_time):
                    delivery = TruckService(truck, self.map)
                    empty = delivery.deliver_a_package()
                    if empty is True:
                        print(f"Truck {truck.name} completed trip, total distance: {truck.distance}")
                        self.delivered_trucks.append(truck)
                        self.trucks.remove(truck)
                        if len(self.pending_trucks) > 0:
                            _truck = self.pending_trucks.pop(0)
                            self.trucks.append(_truck)
                            print(f"Truck {_truck.name} is now delivering")
            self.increaseTime()
            if (self.current_time == self.stop_time):
                self.printAllDetails()
                #TODO:make
                return None
            if self.update_status != "Complete":
                if self.current_time >= self.update_data.time:
                    print(f"package update has occurred")
                    self.updatePackage()
                    self.update_status = "Complete"
        # while trucks are not empty
        return self.delivered_trucks

    def updatePackage(self):
        for truck in self.trucks:
            if self.update_data.package.ID in truck.package_IDs:
                vals = self.update_data.get_values()
                truck.packages.remove(self.update_data.package.ID)
                truck.packages.insert(self.update_data.package.ID, vals)

    def increaseTime(self):
        truck_count = len(self.trucks)
        over_count = 0
        for truck in self.trucks:
            if truck.time > self.current_time:
                over_count += 1
        if truck_count == over_count:
            self.current_time += datetime.timedelta(minutes=15)
            print(f"time is now: {self.current_time}")
