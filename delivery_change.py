import datetime
from Package import Package

#Turns update into object
class PackageUpdate:
    def __init__(self, id, address, hour, min):
        self.address = address
        self.id = int(id)
        self.time = datetime.timedelta(hours=hour, minutes=min)

