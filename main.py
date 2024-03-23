from load_packages import get_packages
from load_packages import loadTrucks
from delivery_service import deliverPackages
from Distances import get_distances

def main():
    packages = get_packages()
    trucks = loadTrucks(packages)
    travel_map = get_distances()
    deliverPackages(trucks, travel_map)
    print(trucks)
    #TODO: instead of 'running', build array of package order, then give to interface to use?

main()

