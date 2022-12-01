from avl_node import AVLNode

nodes_list = []

class AVLTree:

    def __init__(self):
        """Default constructor. Initializes the AVL tree.
        """
        self.root = None
        self.size = 0

    def get_tree_root(self):
        """
        Method to get the root node of the AVLTree
        :return AVLNode -- the root node of the AVL tree
        """
        return self.root

    def get_tree_height(self):
        """Retrieves tree height.
        :return -1 in case of empty tree, current tree height otherwise.
        """
        if self.root is None:
            return -1
        else:
            return self.root.height

    def get_tree_size(self):
        """Yields number of key/value pairs in the tree.
        :return Number of key/value pairs.
        """
        return self.size

    def print_in_preorder(self, root):
        """Traverses the tree in preorder: root, left, right
        :param root: the node we are traversing the tree with
        """
        if root is None:
            return
        nodes_list.append(root.key)
        self.print_in_preorder(root.left)
        self.print_in_preorder(root.right)

    def to_array(self):
        """Yields an array representation of the tree's values (pre-order).
        :return Array representation of the tree values.
        """
        if self.root is None:
            return None
        else:
            self.print_in_preorder(self.root)
            return nodes_list

    def to_array_tree(self,t0,a,t1,b,t2,c,t3):
        """Creates and returns an array with the components of the tree used in rebalancing (rotations)
        :return: List with the 7 components (tree traversed in inorder) used when rotations are performed
        """
        array_values = [t0, a, t1, b, t2, c, t3]
        return array_values

    def find_by_key(self, key):
        """Returns value of node with given key.
        :param key: Key to search.
        :return Corresponding value if key was found, None otherwise.
        :raises ValueError if the key is None
        """
        if key is None:
            raise ValueError("Key is None")
        else:
            return self.search_key(self.root, key)

    def search_key(self, node, key):
        """Finds the key of the node we are searching
        :param node: the node we are traversing the tree with - root initially
        :param value:the key we are searching for
        :return: None if node is None; otherwise, key of the node if the key searched is found; also it return the tree traversal
        meaning, if the key is less than the current node's key, it goes to left, otherwise, it goes to right
        """
        if node is None:
            return None
        if key == node.key:
            return key
        elif key < node.key and node.left is not None:
            return self.search_key(node.left, key)
        elif key > node.key and node.right is not None:
            return self.search_key(node.right, key)

    def insert(self, key, value):
        """Inserts a new node into AVL tree.
        :param key: Key of the new node.
        :param value: Data of the new node. Must not be None. Nodes with the same key
        are not allowed. In this case False is returned. None-Keys and None-Values are
        not allowed. In this case an error is raised.
        :return True if the insert was successful, False otherwise.
        :raises ValueError if the key or value is None.
        """
        if key is None or value is None:
            raise ValueError("None-keys and none-values are not allowed")

        if self.root is None:
            self.root = AVLNode(key, value)
            self.size += 1
            return True
        else:
            rez = self.insert_node(self.root, key, value)
            if rez == False:
                return rez
            self.size += 1
            return True

    def insert_node(self, node, key, value):
        """Insert new node with key=key and value=value
        :param node: the node we are traversing the tree with - firstly, it is the root
        :param key: the key of the new node
        :param value: the value of the new node
        :return: False if the node could not be inserted i.e. the key already exists in the tree
        """
        if key < node.key:
            if node.left is None:
                node.left = AVLNode(key, value)
                node.left.parent = node
                self.insert_node_checking_avl_properties(node.left)
            else:
                self.insert_node(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = AVLNode(key, value)
                node.right.parent = node
                self.insert_node_checking_avl_properties(node.right)
            else:
                self.insert_node(node.right, key, value)
        else:
            return False

    def insert_node_checking_avl_properties(self, node, path=[]):
        """Assures the tree is balanced after insertion
        :param node: the node whose grandfather is unbalanced
        :param path: is contains the nodes traversed: grandfather, father, child - in this order
        """
        if node.parent is None:
            return
        path = [node] + path

        left_height = self.get_current_node_height(node.parent.left)
        right_height = self.get_current_node_height(node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [node.parent] + path
            self.rebalancing(path[2], path[1], path[0])
            return

        new_height = 1 + node.height
        if new_height > node.parent.height:
            node.parent.height = new_height
        self.insert_node_checking_avl_properties(node.parent, path)

    def get_current_node_height(self, node):
        if node is None:
            return -1
        return node.height

    def rebalancing(self, x, y, z):
        """Performs the rotations in order to have the tree balanced
        :param x: the node whose grandfather is unbalanced
        :param y: father of the node
        :param z: grandfather
        :return: the rotation has been performed - subtree is now balanced, later rotations might be performed
        """
        if y == z.left and x == y.left:
            self.right_rotation(z)
        elif y == z.left and x == y.right:
            self.left_rotation(y)
            self.right_rotation(z)
        elif y == z.right and x == y.right:
            self.left_rotation(z)
        elif y == z.right and x == y.left:
            self.right_rotation(y)
            self.left_rotation(z)

    def right_rotation(self, z):
        """Performs the rotation to right
        :param z: the node unbalanded - grandfather
        :return: rotation to right performed
        """
        head = z.parent
        y = z.left
        t3 = y.right
        y.right = z
        z.parent = y
        z.left = t3
        if t3 is not None:
            t3.parent = z
        y.parent = head
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_current_node_height(z.left), self.get_current_node_height(z.right))
        y.height = 1 + max(self.get_current_node_height(y.left), self.get_current_node_height(y.right))

    def left_rotation(self, z):
        """Performs the rotation to left
        :param z: the node unbalanded - grandfather
        :return: rotation to left performed
        """
        head = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2
        if t2 is not None:
            t2.parent = z
        y.parent = head
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_current_node_height(z.left), self.get_current_node_height(z.right))
        y.height = 1 + max(self.get_current_node_height(y.left), self.get_current_node_height(y.right))

    def get_height(self, node):
        """Returns the height of a node
        :param node: the node whose height we would like to find
        :return: the height of node "node"; 0 if the node is None
        """
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        """Returns the balanced of a node
        :param node: the node whose balanced we would like to find
        :return: balance of a node - the difference between the height of the left subtree and the right subtree
        """
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def remove_by_key(self, key):
        """Removes node with given key.
        :param key: Key of node to remove.
        :return True If node was found and deleted, False otherwise.
        @raises ValueError if the key is None.
        """
        if key is None:
            raise ValueError("Key is None")
        rez = self.delete_node(self.find(key))
        if rez is None:
            return False
        return True

    def find(self, key):
        """Find the node with key equal to the parameter "key"
        :param key: the key for the node we are trying to find
        :return: self.find_node(key,self.root) if the tree is not empty, None otherwise
        """
        if self.root is not None:
            return self.find_node(key, self.root)
        else:
            return None

    def find_node(self, key, node):
        """Another function for searching hence this returns the node, not just the value as before in find_by_key()
        :param key: value of the node searched
        :param node: initially the root, then the nodes traversed
        :return: the node whose key is the same as value
        """
        if key == node.key:
            return node
        elif key < node.key and node.left is not None:
            return self.find_node(key, node.left)
        elif key > node.key and node.right is not None:
            return self.find_node(key, node.right)

    def get_successor(self, node):
        """Returns the predecessor of the node (found in the left-most position in the right subtree) passed as argument
        :param node: the node that we want to delete
        :return: the predecessor i.e. the node with the lowest key higher than the current node
        """
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def get_number_of_children(self, node):
        """Finds the number of children of a node
        :param node: the node whose number of children we want to find out
        :return: number of children of node
        """
        children = 0
        if node.left is not None:
            children += 1
        if node.right is not None:
            children += 1
        return children

    def delete_node(self, node):
        """Deletes node. There are three cases:
        i) if the node has no children, we just delete the node
        ii) if the node has one child, it will be replaced by its child
        iii) if the node has two children, it will be replaced by its successor
        After deletion, the property of the AVL tree will be checked - if it is still balanced
        It will be balanced if not.
        :param node: the node we want to delete
        :return: node has been deleted; None if node does not exist or if node is None; True if the deletion was successful
        """
        if node is None or self.find(node.key) is None:
            return None

        parent = node.parent
        node_children = self.get_number_of_children(node)

        if node_children == 0:
            if parent is not None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        if node_children == 1:

            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if parent is not None:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

            child.parent = parent

        if node_children == 2:
            successor = self.get_successor(node.right)
            node.key = successor.key
            self.delete_node(successor)
            return True

        if parent is not None:
            parent.height = 1 + max(self.get_current_node_height(parent.left), self.get_current_node_height(parent.right))
            self.size -= 1
            self.check_tree_after_deletion(parent)
            return True

    def check_tree_after_deletion(self, node):
        """Verifies the AVL property after deletion
        :param node: the parent of the node to be deleted
        :return: subtree is balanced after deletion - later rotations might be performed
        """
        if node is None:
            return

        left_height = self.get_current_node_height(node.left)
        right_height = self.get_current_node_height(node.right)

        if abs(left_height - right_height) > 1:
            y = self.get_child(node)
            x = self.get_child(y)
            self.rebalancing(x, y, node)

        self.check_tree_after_deletion(node.parent)

    def get_child(self, node):
        """Retuns the taller child of the node from the previous function
        :param node: the node from the previous function
        :return: the taller of the two children; left or right
        """
        left = self.get_current_node_height(node.left)
        right = self.get_current_node_height(node.right)
        if left >= right:
            return node.left
        return node.right