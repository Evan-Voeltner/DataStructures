class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, node_value):
        new_treenode = TreeNode(node_value)
        if self.root == None:
            self.root = new_treenode
            print(f'Root node created with a value of {node_value}')
            return

        current_node = self.root
        node_placed = False
        while node_placed == False:
            if current_node.value < node_value:
                if current_node.greater_child == None:
                    current_node.greater_child = new_treenode
                    node_placed = True
                    print(f'Greater child node created with a value of {node_value} for the parent {current_node.value}')
                else:
                    current_node = current_node.greater_child  
            
            elif current_node.value > node_value:
                if current_node.lesser_child == None:
                    current_node.lesser_child = new_treenode
                    node_placed = True
                    print(f'Lesser child node created with a value of {node_value} for the parent {current_node.value}')
                else:
                    current_node = current_node.lesser_child
                    
        

    def search_for_node(self):
        pass

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.lesser_child = None
        self.greater_child = None