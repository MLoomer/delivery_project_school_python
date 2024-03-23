#Michael Loomer - 001305152
from load_packages import get_packages
from load_packages import loadTrucks
from Distances import get_distances
from delivery_service import DeliveryService
from delivery_change import PackageUpdate

def main():
    packages = get_packages()
    trucks = loadTrucks(packages)
    travel_map = get_distances()
    package_update = PackageUpdate(9, "410 S State St", "Salt Lake City", "UT",
                                   84103, "EOD", 2, 10, 20)
    delivery = DeliveryService(trucks, travel_map, 8, package_update)
    finished_trucks = delivery.deliverPackages()
    sum = 0
    for truck in finished_trucks:
        print(f"{truck}")
        sum += truck.distance
    print(f"total distance: {sum}")

    #TODO: Way to see status of any specific package. By ID maybe?
    #see status of eevry package at specifc times
        #input a time for when to stop, print all package status
    #comment my code

    #package specifics


main()

