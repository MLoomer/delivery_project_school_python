#my own hash table
class HashTable:
    # create table, set size to max truck size unless otherwise stated
    def __init__(self, size=16):
        self.list = []
        for i in range(size):
            self.list.append([])

    # hash funct since repeated use
    def hashBucket(self, key):
        bucketNum = hash(key) % len(self.list)
        bucket = self.list[bucketNum]
        return bucket

    #remove from table
    def remove(self, key):
        bucket = self.hashBucket(key)
        for item in bucket:
            if item[0] == key:
                bucket.remove(item)

    #looks up id
    def lookup(self, key):
        bucket = self.hashBucket(key)
        for item in bucket:
            if item[0] == key:
                return item[1]
        return None

    # insert package by ID
    def insert(self, key, value):
        bucket = self.hashBucket(key)
        # check if item already exists
        for item in bucket:
            if item[0] == key:
                item[1] = value
                return True
        # otherwise append to end
        bucket.append((key, value))
        return True