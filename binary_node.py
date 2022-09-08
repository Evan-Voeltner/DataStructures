class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, node_value):
        new_treenode = TreeNode()
        if self.root == None:
            self.root = new_treenode
            return
        
        

    def search_for_node(self):
        pass

class TreeNode:
    def __init__(self):
        self.value = None
        self.parent = None
        self.lesser_child = None
        self.greater_child = None 