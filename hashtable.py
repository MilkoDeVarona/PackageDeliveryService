# HashTable class using chaining for collision handling
# Source: WGU Zybooks
class HashTable:
    # Constructor with initial capacity parameter of 50 buckets
    # Total number of packages is 40, therefore the table will only be 80% full
    # Assigns all buckets on the table with an empty list
    # O(n) linear time
    def __init__(self, capacity=50):
        # initializes the hash table with empty bucket list entries
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Inserts a new item into the hash table or updates an existing item
    # O(n) linear time
    def insert(self, key, item):
        # gets the location in the table where this item will go
        package_location = hash(key) % len(self.table)
        package_list = self.table[package_location]

        # updates key if it is already in the list
        for p in package_list:
            if p[0] == key:
                p[1] = item
                return True

        # if not in the list, inserts the item to the end of the bucket list
        key_value = [key, item]
        package_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table
    # Returns the item if found, or None if not found
    # O(n) linear time.
    def search(self, key):
        # gets the location where this key would be.
        package_location = hash(key) % len(self.table)
        package_list = self.table[package_location]

        # searches for the key in the bucket list
        for p in package_list:
            if p[0] == key:
                return p[1]  # returns value
        return None

    # Removes an item with matching key from the hash table
    # O(n) linear time
    def remove(self, key):
        # gets the location where this item will be removed from
        package_location = hash(key) % len(self.table)
        package_list = self.table[package_location]

        # removes the item from the bucket list if it is present
        for p in package_list:
            if p[0] == key:
                package_list.remove([p[0], p[1]])
