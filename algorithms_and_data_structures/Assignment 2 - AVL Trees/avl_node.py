class AVLNode:
    def __init__(self, key=0, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    def to_string(self):
        return "key:" + str(self.key) + ", value: " + str(self.value)