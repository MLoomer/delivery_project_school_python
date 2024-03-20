from load_packages import get_packages
from load_packages import loadTrucks
from delivery_service import deliverPackages
from Distances import get_travel_map

def main():
    packages = get_packages()
    trucks = loadTrucks(packages, get_travel_map())
    print(trucks[1].map)
    #deliverPackages(trucks, travel_map)
    print(trucks)


main()

