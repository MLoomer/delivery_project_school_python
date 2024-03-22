
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

def get_remaining_id_addresses(truck):
    remaining_addresses = []
    for id in truck.package_IDs:
        addr = truck.packages.lookup(id)[0]
        remaining_addresses.append([id, addr])
    return remaining_addresses

def get_remaining_addresses(remaining_addresses):
    arr = []
    for address in remaining_addresses:
        arr.append(address[1])
    return arr

def get_row_index(value, arr):
    for i, row in enumerate(arr):
        if value in row[0]:
            return i-1

def getXYValue(rowInd, i, valuemap):
    #print(f"rowInd {rowInd}, i = {i}")
    #print(f"travelmap: {valuemap[rowInd]}")
    if valuemap[rowInd][i] == "":
        return valuemap[i][rowInd]
    return valuemap[rowInd][i]

def remove_labels(travel_map):
    arr = []
    rowOffset = 1
    value_map = travel_map.copy()
    colOffset = 2
    for i in range(len(value_map)):
        if (i > 0):
            arr.append(value_map[i][colOffset:])
    return rowOffset, colOffset, arr

def get_address(index, travel_map):
    return travel_map[0][index]

def get_matching_ids(address, id_address):
    arr = []
    for row in id_address:
        if address in row[1]:
            arr.append(row[0])
    return arr


def strip(address):
    return address.split("\n")[1].lstrip()

def nearest_drive_alg(current_address, remaining_addresses, travel_map):
    rowInd = get_row_index(current_address, travel_map)
    min = 9999
    index = 9999
    rowOffset, colOffset, valuemap = remove_labels(travel_map)
    #print(f"colOffset: {colOffset}, rowOffset: {rowOffset}, valuemap: {valuemap}")
    for i in range(len(valuemap[rowInd])):
        value = float(getXYValue(rowInd, i, valuemap))
        if (value < min) and (rowInd != i):
            addrr = strip(get_address(i+colOffset, travel_map))
            if addrr in remaining_addresses:
                min = value
                index = i
    if (index == 9999): print("failed to find match")
    new_address = strip(get_address(index+colOffset, travel_map))
    print(new_address)
    return new_address, min

def deliver_a_package(truck, travel_map):
    current_address = truck.address
    id_address = get_remaining_id_addresses(truck)
    remaining_addresses = get_remaining_addresses(id_address)
    address_to_go, distance = nearest_drive_alg(current_address, remaining_addresses, travel_map)
    #return header (addr) and place as current address
    truck.address = address_to_go
    truck.distance += float(distance)
    print(f"delivered to {truck.address}, distance is {truck.distance}")
    truck.removePackages(get_matching_ids(truck.address, id_address))
    if (len(truck.package_IDs) == 0): return True