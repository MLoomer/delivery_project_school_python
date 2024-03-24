

from load_packages import get_packages
from load_packages import loadTrucks
from Distances import get_distances
from delivery_service import DeliveryService
from delivery_change import PackageUpdate

##
# Runs Delivery Program
##
def main():
    #Get packages
    packages = get_packages()

    #Load packages onto trucks
    trucks = loadTrucks(packages)

    #create distance map
    travel_map = get_distances()

    #load package change data
    package_update = PackageUpdate(9, "410 S State St",10, 20)
    val = input("Is there a specific time you want to stop to see route info? If so, enter a hour and minute in format of: #:##, in intervals of 15min. Otherwise hit enter\n")

    #Set up delivery
    delivery = DeliveryService(trucks, travel_map, 8, package_update, val, 1)

    #Run delivery
    delivery.deliverPackages()

main()