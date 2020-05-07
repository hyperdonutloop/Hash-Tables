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
        # self.total_items = 0
        # self.load_factor = 0

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


        # index = the index of whatever the hash function came up with
        index = self.hash_index(key)
        # setting the node to iterate through linked list
        # assigning node to whatever index it needs to be at
        node = self.storage[index]
        # if there are no other values at this index
        if node is None:
            # set storage at the hashed index to the key/value
            # appending the key, value pairs at that index
            self.storage[index] = HashTableEntry(key, value)
            return
        # otherwise
        # initializing prev, so you can set next node
        prev = None
        # while there is a value there
        while node is not None:
            # initializing prev to node
            prev = node
            # appending the node as the node.next
            node = node.next
        # if the nodes key matches the input key
            if prev.key == key:
            # update the node's value
                prev.value = value
                return
            
        # now assigning the key,value to the new node spot
        prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # When you delete():
        #   if the load < 0.2:
        #       if size > minimum (8):
        #         halve the size of the hashtable down (to the minimum, at most)
        
        # index = the index of whatever the hash function came up with - should always be the same
        index = self.hash_index(key)
        # setting the node so that we can iterate through if there are collisions
        node = self.storage[index]

        prev = None
        # if there is data at this node, loop through until you get a key that matches or node is None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # if there is nothing
        if node is None:
            # return this
            return 'No key found here'
        # if the key matches, delete the node entirely
        # this is also saying if node.key == key
        else: 
            if prev is None: 
                self.storage[index] = node.next
            else: 
                prev.next = node.next
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # index = the index of whatever the hash function came up with - should always be the same
        index = self.hash_index(key)
        # if the index is there
        node = self.storage[index]
        # if there is nothing at the index
        if self.storage[index] is None:
            # return none
            return None
        # while node is not none and the key is not found
        while node is not None and key != node.key:
            # update next pointer
            node = node.next
        # then we check if node is not None
        if node is None:
            # return none
            return None
        # otherwise, this means key is found, so return value
        return node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # make a new/bigger table
        # go through all the old elements and hash into new list
        old_stuff = self.storage
        self.capacity = self.capacity * 2
        new_stuff = [None] * self.capacity
        self.storage = new_stuff

        self.size = 0

        for item in old_stuff:
            if item is not None:
                while item is not None:
                    self.put(item.key, item.value)
                    item = item.next


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
