
def deliverPackages(trucks, travel_map):
    for truck in trucks:
        empty = deliver_a_package(truck, travel_map)
        if empty is True:
            trucks.remove(truck)
    # while trucks are not empty
    if trucks:
        deliverPackages(trucks, travel_map)
    else:
        return None

def get_remaining_addresses(truck):
    remaining_addresses = []
    for id in truck.package_IDs:
        addr = truck.packages.lookup(id)[0]
        remaining_addresses.append(addr)
    return remaining_addresses


def get_row_index(value, arr):
    for i, row in enumerate(arr):
        if value in row[0]:
            return i

def getXYValue(rowInd, i, valuemap):
    print(f"rowInd {rowInd}, i = {i}")
    print(f"travelmap: {valuemap[rowInd]}")
    if valuemap[rowInd][i] == "":
        return valuemap[i][rowInd]
    return valuemap[rowInd][i]

def remove_labels(travel_map):
    arr = []
    for i in range(len(travel_map)):
        if (i >= 0):
            arr.append(travel_map[i][2:])
    return arr

def get_address(index, travel_map):
    return travel_map[0][index]

def nearest_drive_alg(current_address, remaining_addresses, travel_map):
    rowInd = get_row_index(current_address, travel_map)
    min = 12 #TODO: FIX
    valuemap = remove_labels(travel_map)
    for i in range(len(valuemap[rowInd])):
        value = float(getXYValue(rowInd, i, valuemap))
        if value < min:
            if i != rowInd:
                min = value
                index = i
    print(f"min value is {min} and index is {index}")
    new_address = get_address(index, travel_map)
    return new_address

def deliver_a_package(truck, travel_map):
    print("delivered something")
    current_address = truck.address
    remaining_addresses = get_remaining_addresses(truck)
    address_to_go = nearest_drive_alg(current_address, remaining_addresses, travel_map)
    # cross reference to sheet for distances
    # get shortest #
    #return header (addr) and place as current address
    # add distance
    # remove package

        #print(f"current_address {current_address}")
        #key, distance, package = get_shortest_distance(travel_map.lookup(int(current_address)), truck)
        #print(f"key {key}, distance {distance}, package {package}")
        #truck.address = key
        #truck.distance += float(distance)
        #truck.removePackage(package)
    #if last package
    return True
