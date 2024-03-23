import csv
from Truck import Truck
from HashTable import HashTable
def get_packages():
    with open("packages_csv.csv") as file:
        csv_reader = csv.reader(file, delimiter=",")
        # Skip header
        next(csv_reader)

        packages = []
        for package in csv_reader:
            packages.append(package)
    return packages


def loadTrucks(packages):
    truckOnePackageIDs = [30, 31, 34, 37, 40, 2, 4, 5, 7, 8, 10, 11, 12, 17, 19, 21]
    truckTwoPackageIDs = [3, 18, 36, 38, 6, 25, 28, 32, 20, 16, 14, 9, 15, 1, 13, 29]
    truckThreePackageIDs = [21, 22, 23, 24, 26, 27, 33, 35, 39]
    #truckOnePackageIDs = [31, 33]
    #truckTwoPackageIDs = [3, 18, 36]
    #truckThreePackageIDs = [21, 22, 23]

    # create trucks
    trucks = [Truck("A", 16), Truck("B", 16), Truck("C", 16)]

    package_assignments = {
        trucks[0]: truckOnePackageIDs,
        trucks[1]: truckTwoPackageIDs,
        trucks[2]: truckThreePackageIDs,
    }
    for package in packages:
        for i in range(3):
            if int(package[0]) in package_assignments[trucks[i]]:
                print(f"placed package {package[0]} on truck {i}")
                trucks[i].loadPackage(package)
                break
    return trucks
