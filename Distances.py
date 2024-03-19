import csv
from HashTable import HashTable

def get_distances():
    with open("distances_csv.csv") as file:
        csv_reader = csv.reader(file, delimiter=",")
        # Skip header
        distances = HashTable(26)
        i = 0
        next(csv_reader)
        for address in csv_reader:
            address, *dist = address
            distances.insert(i, dist)
            i += 1
    return distances

