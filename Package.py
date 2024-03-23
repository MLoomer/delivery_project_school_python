class Package:

    def __init__(self, arr):
        self.ID = arr[0]
        self.address = arr[1]
        self.city = arr[2]
        self.state = arr[3]
        self.zip = arr[4]
        self.deadline = arr[5]
        self.weight = arr[6]
        self.notes = arr[7]
        self.status = "HUB"


