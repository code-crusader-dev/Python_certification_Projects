** start of main.py **

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value

    def add(self, key, value):
        hash_key = self.hash(key)

        if hash_key not in self.collection:
            self.collection[hash_key] = {}

        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)

        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                del self.collection[hash_key][key]

                if len(self.collection[hash_key]) == 0:
                    del self.collection[hash_key]

    def lookup(self, key):
        hash_key = self.hash(key)

        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                return self.collection[hash_key][key]

        return None


** end of main.py **

