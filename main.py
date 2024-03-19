from load_packages import get_packages
from load_packages import loadTrucks
from Distances import get_distances


def main():
    packages = get_packages()
    trucks = loadTrucks(packages)
    print(trucks)

main()


# for each package in truck
#check distance from current location
# go to closest location
#function to extract shortest distance
#function ti get shortest time
#function to decide which to get - shortest distance or time
#function to extract distance of time constrant