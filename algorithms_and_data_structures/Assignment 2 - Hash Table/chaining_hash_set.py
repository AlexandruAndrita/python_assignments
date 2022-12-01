import chaining_hash_node

class ChainingHashSet():
    def __init__(self, capacity=0):
        self.hash_table = [None] * capacity
        self.table_size = 0
        self.capacity = capacity

    def get_hash_code(self, key):
        """Hash function that calculates a hash code for a given key using the modulo division.
        :param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        :return:
        		The calculated hash code for the given key.
        """
        return key%self.capacity

    def get_hash_table(self):
        """(Required for testing only)
        :return the hash table.
        """
        return self.hash_table

    def set_hash_table(self, table):
        """(Required for testing only) Set a given hash table..
        :param table: Given hash table which shall be used.

        !!!
        Since this method is needed for testing we decided to implement it.
        You do not need to change or add anything.
        !!!

        """
        self.hash_table = table
        self.capacity = len(table)
        self.table_size = 0
        for node in table:
            while node is not None:
                self.table_size += 1
                node = node.next

    def get_table_size(self):
        """returns the number of stored keys (keys must be unique!)."""
        return self.table_size

    def insert(self, key):
        """Inserts a key and returns True if it was successful. If there is already an entry with the
          same key, the new key will not be inserted and False is returned.
         :param key:
         		The key which shall be stored in the hash table.
         :return:
         		True if key could be inserted, or False if the key is already in the hash table.
         :raises:
         		a ValueError if any of the input parameters is None.
         """
        if key is None:
            raise ValueError("parameter key is None")
        if self.contains(key) is False:
            self.table_size+=1
            position=self.get_hash_code(key)
            current_node=self.hash_table[position]
            if current_node is None:
                #there are no other values already placed on this position
                self.hash_table[position]=chaining_hash_node.ChainingHashNode(key)
                return True

            #there are already other values placed on the position we want to insert to
            previous_node=current_node
            while current_node is not None:
                previous_node=current_node
                current_node=current_node.next

            previous_node.next=chaining_hash_node.ChainingHashNode(key)
            return True
        else:
            return False

    def contains(self, key):
        """Searches for a given key in the hash table.
         :param key:
         	    The key to be searched in the hash table.
         :return:
         	    True if the key is already stored, otherwise False.
         :raises:
         	    a ValueError if the key is None.
         """
        if key is None:
            raise ValueError("parameter key is None")
        position=self.get_hash_code(key)
        current_node=self.hash_table[position]
        while current_node is not None:
            if current_node.key==key:
                return True
            current_node=current_node.next
        return False

    def remove(self, key):
        """Removes the key from the hash table and returns True on success, False otherwise.
        :param key:
        		The key to be removed from the hash table.
        :return:
        		True if the key was found and removed, False otherwise.
        :raises:
         	a ValueError if the key is None.
        """
        if key is None:
            raise ValueError("parameter key is None")
        position=self.get_hash_code(key)
        current_node=self.hash_table[position]
        previous_node=None
        while current_node is not None:
            if current_node.key==key:
                break
            previous_node=current_node
            current_node=current_node.next

        #the node we are trying to delete does not exist (node is None)
        if current_node is None:
            return False
        else:
            self.table_size-=1
            if previous_node is None:
                #the node we are deleting does not have a "next" member (i.e. there is no list for that position
                #from the hash)
                self.hash_table[position]=current_node.next
            else:
                #the node we are deleting is part of a list for that position in the hash
                previous_node.next=current_node.next
            return True

    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        position = 0
        initial_capacity=self.capacity
        while position < initial_capacity:
            current_node = self.hash_table[position]
            if current_node.next is not None:
                #there is a list on that position
                while current_node is not None:
                    self.remove(current_node.key)
                    current_node = current_node.next
            else:
                #no list on that position
                self.remove(current_node.key)
            position += 1
        self.capacity=0

    def to_string(self):
        """Returns a string representation of the hash table (array indices and stored keys) in the format
            Idx_0 {Node, Node, ... }, Idx_1 {...}
            e.g.: 0 {13}, 1 {82, 92, 12}, 2 {2, 32}, """
        position=0
        hash_table=""
        while position<self.capacity:
            hash_table+=str(position)
            current_node=self.hash_table[position]
            hash_table+=" {"
            while current_node is not None:
                hash_table+=str(current_node.key)
                if current_node.next is not None:
                    hash_table+=", "
                current_node=current_node.next
            hash_table+="}"
            if position<self.capacity-1:
                hash_table+=", "
            position+=1
        return hash_table

