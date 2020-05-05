class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        # creating an array with nones
        self.capacity = capacity
        self.storage = [None] * self.capacity
        # self.size = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        
        # index = self.hash_index(key)
        # # the storage of that index is the key and the value
        # self.storage[index] = (key, value)

        # index = the index of whatever the hash function came up with
        index = self.hash_index(key)
        # setting the node to iterate through linked list
        node = self.storage[index]
        # if there are no other values at this index
        if node is None:
            # set storage at the hashed index to the key/value
            # placing the key, value pairs at that index
            self.storage[index] = HashTableEntry(key, value)
            return
        # otherwise
        # if there ARE nodes at this index
        prev = node
        # iterate through all nodes, while next is not None and node's key does not equal input key
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # if the nodes key matches the input key
        if prev.key == key:
            # update the node's value
            prev.value = value
            return
        else: 
            # otherwise, create and insert a new entry for the last node
            prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # index = the index of whatever the hash function came up with - should always be the same
        index = self.hash_index(key)
        # taking that index value and assigning it to None removing key and value
        self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # index = the index of whatever the hash function came up with - should always be the same
        index = self.hash_index(key)
        # if the index is there
        if self.storage[index] is not None:
            # return the value
            return self.storage[index][1]
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
