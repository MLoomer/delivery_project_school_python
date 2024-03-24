import datetime

#Class made for data manipulation that doesnt need class objects
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

#Truck service class for some truck specific functions
class TruckService:
    def __init__(self, truck, map):
        self.truck = truck
        self.map = map
        self.rowOffset, self.colOffset, self.valuemap = self.remove_labels()

    def get_remaining_id_addresses(self):
        remaining_addresses = []
        for id in self.truck.package_IDs:
            package = self.truck.packages.lookup(id)
            addr = package.address
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

    #methos to deliver a package
    def deliver_a_package(self):
        data = ValueService()
        #get next address + distance based on nearest neighbor
        current_address = self.truck.address
        id_address = self.get_remaining_id_addresses()
        remaining_addresses = self.get_remaining_addresses(id_address)
        address_to_go, distance = self.nearest_drive_alg(current_address, remaining_addresses)

        #assign changes to truck
        self.truck.address = address_to_go
        self.truck.distance = round(float(distance) + self.truck.distance, 2)
        self.truck.time += datetime.timedelta(hours=distance / 18)

        #deliver packages with matching addresses
        ids = data.get_matching_ids(self.truck.address, id_address)
        self.truck.removePackages(ids, self.truck.time)
        print(f"Truck {self.truck.name} delivering package(s) {ids} to {self.truck.address}, traveling {float(distance)}, distance is {self.truck.distance}, arrival will be at {self.truck.time}")

        #if no more packages, return True, otherwise returning none
        if (len(self.truck.package_IDs) == 0): return True

    #function to find lowest value from list
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
        #return address of lowest match
        if (index is None): print("failed to find match")
        new_address = data.get_address(index + self.colOffset, self.map)
        return new_address, min

#Delivery service
class DeliveryService:
    def __init__(self, trucks, map, start_time_hours, update, stoptime, interval):
        data = ValueService()
        self.trucks = trucks
        self.pending_trucks = self.driver_limit()
        self.map = map
        self.delivered_trucks = []
        self.current_time = datetime.timedelta(hours=start_time_hours)
        self.update_data = update
        self.update_status = ""
        self.interval = interval
        if (stoptime == ""):
            self.stop_time = ""
        else:
            hour, min = data.formatTime(stoptime)
            self.stop_time = datetime.timedelta(hours=hour, minutes=min)
        self.min_time = None
        self.index = None

    #prints all data at the end
    def printAllDetails(self):
        print(f"FINAL STATS:")
        #print all package statuses
        trucks = self.trucks + self.delivered_trucks + self.pending_trucks
        sum = float(0)
        for truck in trucks:
            print(f"TRUCK {truck.name} total distance: {truck.distance}")
            sum += truck.distance
            for id in truck.ids:
                package = truck.packages.lookup(id)
                if package.status != "DELIVERED":
                    status = package.status
                elif package.delivery_time > self.stop_time:
                    status = f"EN ROUTE TO BE DELIVERED (NEXT STOP)"
                else:
                    status = f"DELIVERED at {package.delivery_time}"
                print(id, status)
        print(f"Total Distance {sum}")
        #print all truck distances
        #print combined distances
        return None

    #adds 3rd truck
    def driver_limit(self):
        arr = []
        for truck in self.trucks:
            if truck.name == "3":
                self.trucks.remove(truck)
                arr.append(truck)
        return arr

    def set_min_time_and_truck(self):
        truck_times = [truck.time for truck in self.trucks]
        time_index_pairs = [[time, i] for i, time in enumerate(truck_times)]
        self.index = min(time_index_pairs)[1]
        self.min_time = time_index_pairs[self.index][0]

    def update_package_status(self, truck, status):
        if truck.status == "HUB":
            truck.status = status
            truck.update_packages(status)

    #Main functio nfor running the service
    def deliverPackages(self):
        #while trucks exist
        while len(self.trucks):
            #find minimum truck time (basically truck with the oldest stop)
            self.set_min_time_and_truck()
            #while time is under 'current time'
            while self.min_time < self.current_time:

                # if we hit self time constraint, end
                if self.current_time >= self.stop_time:
                    self.printAllDetails()
                    return self.delivered_trucks

                #set up truck
                truck = self.trucks[self.index]

                #sets up truck services
                delivery = TruckService(truck, self.map)

                #updates packages to en route if havent loaded truck before
                self.update_package_status(truck, "EN ROUTE")

                #runs package updater if time
                if self.update_status != "Complete":
                    if self.current_time >= self.update_data.time:
                        print(f"package update has occurred")
                        self.updatePackage()
                        self.update_status = "Complete"

                #deliver a package, check if truck is now empty
                empty = delivery.deliver_a_package()
                #if empty, remove truck from list, check if no more trucks
                if empty is True:
                    print(f"Truck {truck.name} completed trip, total distance: {truck.distance}")
                    self.delivered_trucks.append(truck)
                    self.trucks.remove(truck)
                    if len(self.trucks) == 0: break
                    if len(self.pending_trucks) > 0:
                        _truck = self.pending_trucks.pop(0)
                        self.trucks.append(_truck)
                        print(f"Truck {_truck.name} is now delivering")
                self.set_min_time_and_truck()

            #move time forward if no trucks waiting at stops
            self.increaseTime()

        #if trucks now empty, finish
        self.printAllDetails()
        return None

    #update package data
    def updatePackage(self):
        for truck in self.trucks:
            if self.update_data.id in truck.package_IDs:
                id = self.update_data.id
                package = truck.packages.lookup(id)
                package.address = self.update_data.address

    def increaseTime(self):
        self.current_time += datetime.timedelta(minutes=self.interval)
