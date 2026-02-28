class HashTable:
    def __init__(self):
        # initialize empty dictionary
        self.collection = {}

    # hash method
    def hash(self, key):
        # sum Unicode values of characters
        return sum(ord(char) for char in key)

    # add key-value pair
    def add(self, key, value):
        hashed_key = self.hash(key)

        # create bucket if it doesn't exist
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        # store inside nested dictionary
        self.collection[hashed_key][key] = value

    # remove key-value pair
    def remove(self, key):
        hashed_key = self.hash(key)

        # check if hash bucket and key exist
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

                # optional cleanup if bucket becomes empty
                if not self.collection[hashed_key]:
                    del self.collection[hashed_key]

    # lookup value by key
    def lookup(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key)

        return None