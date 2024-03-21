from load_packages import get_packages
from load_packages import loadTrucks
from delivery_service import deliverPackages
from Distances import get_distances

def main():
    packages = get_packages()
    trucks = loadTrucks(packages)
    travel_map = get_distances()
    deliverPackages(trucks, travel_map)
    ##TODO: We forgot to include the addr row[0] in the travel_map so our #s are off. We need it though to get the next addr.
    #Need to either add it in and fix formulas, or pass header addrs as a parameter
    print(trucks)


main()

