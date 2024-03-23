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
    val = input("Is there a specific time you want to stop to see route info? If so, enter a hour and minute in format of: #:##, in intervals of 15min. Otherwise hit enter\n")
    delivery = DeliveryService(trucks, travel_map, 8, package_update, val)
    finished_trucks = delivery.deliverPackages()
    sum = 0
    for truck in finished_trucks:
        print(f"{truck}")
        sum += truck.distance
    print(f"total distance: {sum}")

    #TODO: Make fucntion printAllDetails() that prints all package status and truck distances
    #comment my code

main()

