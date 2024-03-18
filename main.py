from load_packages import get_packages
from load_packages import loadTrucks


def main():
    packages = get_packages()
    trucks = loadTrucks(packages)
    print(trucks)

main()

    #get packages from csv
    # load trucks while reading packages
    #once packages are loaded, ??