from load_packages import get_packages
from load_packages import loadTrucks
from Distances import get_distances
from delivery_service import DeliveryService

def main():
    packages = get_packages()
    trucks = loadTrucks(packages)
    travel_map = get_distances()
    delivery = DeliveryService(trucks, travel_map, 8)
    finished_trucks = delivery.deliverPackages()
    sum = 0
    for truck in finished_trucks:
        print(f"{truck}")
        sum += truck.distance
    print(f"total distance: {sum}")
    #TODO: instead of 'running', build array of package order, then give to interface to use?

main()

