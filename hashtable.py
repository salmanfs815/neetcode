# https://neetcode.io/problems/hashTable/question

class HashTable:
    
    def __init__(self, capacity: int):
        self.table = [None for i in range(capacity)]
        self.capacity = capacity
        self.size = 0
        self.max_load = 0.5
    
    def hash(self, key: int) -> int:
        return sum([ord(c) for c in str(key)]) % self.capacity

    def insert(self, key: int, value: int) -> None:
        idx = self.getIndex(key)
        if idx != -1:
            self.table[idx] = (key, value)
        else:
            idx = self.hash(key)
            while self.table[idx] != None:
                idx = (idx + 1) % self.capacity
            self.table[idx] = (key, value)
            self.size += 1
            if self.size / self.capacity >= self.max_load:
                self.resize()

    # given key, return index of associated key-value pair
    def getIndex(self, key: int) -> int:
        idx = self.hash(key)
        while True:
            if self.table[idx] == None:
                return -1
            if self.table[idx][0] == key:
                return idx
            idx = (idx + 1) % self.capacity
    
    # given key, return associated value
    def get(self, key: int) -> int:
        idx = self.getIndex(key)
        if idx == -1:
            return -1
        return self.table[idx][1]

    # remove key and return True; False if key not present
    def remove(self, key: int) -> bool:
        idx = self.getIndex(key)
        if idx == -1:
            return False
        self.size -= 1
        self.table[idx] = None
        return True

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    # double capacity
    def resize(self) -> None:
        oldTable = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [None for i in range(self.capacity)]
        for pair in oldTable:
            if pair:
                self.insert(pair[0], pair[1])
