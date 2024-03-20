from Distances import get_shortest_distance

def check_for_empty_trucks(trucks):
    for truck in trucks:
        if len(truck) != 0:
            print(f"truck {truck} is not empty")
            return False
    return True

def deliver_package(truck, travel_map):
    #for now just do shortest distance for understanding
    current_address = truck.address
    print(f"current_address {current_address}")
    key, distance, package = get_shortest_distance(travel_map.lookup(int(current_address)), truck)
    print(f"key {key}, distance {distance}, package {package}")
    truck.address = key
    truck.distance += float(distance)
    truck.removePackage(package)
    #travel_map.remove(package)

    #check package list for times <EOD
    # if exist, work on that in order of shortest
    #if doesnt, get col of lowest dist other than 0

# if packages exist in truck, get package list
# check distance from current location
# go to closest location
#TODO: Work on this

# function to extract shortest distance
# function ti get shortest time
# function to decide which to get - shortest distance or time
# function to extract distance of time constrant


def deliverPackages(trucks, travel_map):
    for truck in trucks:
        deliver_package(truck, travel_map)
        if len(truck) == 0:
            trucks.remove(truck)
    # while trucks are not empty
    if trucks:
        deliverPackages(trucks)
    else:
        return None