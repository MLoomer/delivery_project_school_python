import csv
from Truck import Truck
from Package import Package
from HashTable import HashTable

import datetime
def get_packages():
    with open("packages_csv.csv") as file:
        csv_reader = csv.reader(file, delimiter=",")
        # Skip header
        next(csv_reader)
        packages = []
        for row in csv_reader:
            package = Package(row)
            packages.append(package)
    return packages


def loadTrucks(packages):
    truckOnePackageIDs = [29, 7, 19, 1, 13, 39, 30, 8, 31, 20, 21, 37, 14, 15, 16, 34]
    truckTwoPackageIDs = [27, 35, 18, 36, 3, 33, 11, 17, 40, 4, 38, 5, 24, 23]
    truckThreePackageIDs = [10, 2, 22, 28, 9, 6, 32, 25, 26, 12]
    #truckOnePackageIDs = [31, 33]
    #truckTwoPackageIDs = [3, 18, 36]
    #truckThreePackageIDs = [21, 22, 23]

    truckOneDepartureTime = datetime.timedelta(hours=8)
    truckTwoDepartureTime = datetime.timedelta(hours=8)
    truckThreeDepartureTime = datetime.timedelta(hours=9, minutes=5)

    # create trucks
    trucks = [Truck("1", 16, truckOneDepartureTime, "HUB"),
              Truck("2", 16, truckTwoDepartureTime, "HUB"),
              Truck("3", 16, truckThreeDepartureTime, "HUB")]

    package_assignments = {
        trucks[0]: truckOnePackageIDs,
        trucks[1]: truckTwoPackageIDs,
        trucks[2]: truckThreePackageIDs,
    }
    for package in packages:
        for i in range(3):
            if int(package.ID) in package_assignments[trucks[i]]:
                print(f"placed package {package.ID} on truck {i}")
                trucks[i].loadPackage(package)
                break
    return trucks
