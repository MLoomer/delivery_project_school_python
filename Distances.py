import csv
from HashTable import HashTable

def get_distances_old():
    with open("distances_csv.csv") as file:
        csv_reader = csv.reader(file, delimiter=",")
        # Skip header
        distances = HashTable(26)
        i = 0
        for address in csv_reader:
            address, *dist = address
            distances.insert(i, dist)
            i += 1
    return distances

def get_distances():
    with open("distances_csv.csv") as file:
        csv_reader = csv.reader(file, delimiter=",")
        # Skip header
        distances = []
        for row in csv_reader:
            distances.append(row)
    return distances

def get_shortest_distance(distanceArr, truck):
    packages = truck.packages
    package_ids = truck.package_IDs
    ##TODO: You messed up. You're thinking same num of locations to addresses or something. Need to think this out more
    min_index = 0
    min_distance = distanceArr[int(package_ids[min_index])]
    print(f"# of packages: {len(package_ids)}")
    for i in range(len(package_ids)):
        print(int(package_ids[i]))
        current_distance = distanceArr[int(package_ids[i])]
        print(f"index: {i}, package_ID_Value: {int(package_ids[i])}, mindistance: {min_distance}, current distance: {current_distance}")
        if current_distance < min_distance:
             min_distance = current_distance
             min_index = i
    return [min_index, min_distance, packages.lookup(min_index)]
