import datetime
from Package import Package

class PackageUpdate:
    def __init__(self, id, address, city, state, zip, deadline, weight, hour, min):
        notes = "updated package"
        status = "enroute"
        self.time = datetime.timedelta(hours=hour, minutes=min)
        self.package = Package(id, address, city, state, zip, deadline, weight, notes, status)

    def get_values(self):
        arr = [self.package.address, self.package.city, self.package.state, str(self.package.zip),
               self.package.deadline, str(self.package.weight), self.package.notes]
        return arr
