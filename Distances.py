import csv

def get_distances():
    with open("distances_csv.csv") as file:
        csv_reader = csv.reader(file, delimiter=",")
        # Skip header
        distances = []
        for row in csv_reader:
            distances.append(row)
    return distances
