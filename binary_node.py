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
                    current_node.greater_child.parent = current_node
                    node_placed = True
                    print(f'Greater child node created with a value of {node_value} for the parent {current_node.value}')
                else:
                    current_node = current_node.greater_child  
            
            elif current_node.value > node_value:
                if current_node.lesser_child == None:
                    current_node.lesser_child = new_treenode
                    current_node.lesser_child.parent = current_node
                    node_placed = True
                    print(f'Lesser child node created with a value of {node_value} for the parent {current_node.value}')
                else:
                    current_node = current_node.lesser_child
                    
    def print_node_info(self, node):
        lesser_child = ''
        greater_child = ''
        if node.lesser_child != None:
            lesser_child =  f'| Lesser Child {node.lesser_child.value} '
        if node.greater_child != None:
            greater_child =  f'| Greater Child {node.greater_child.value} '
        print(f'Value {node.value} | Parent {node.parent.value} ' + lesser_child + greater_child)

    def search_for_node(self, value_to_find):
        current_node = self.root
        while True:
            if current_node.value == value_to_find:
                print('Node Found')
                self.print_node_info(current_node)
                return 
            elif current_node.value < value_to_find:
                if current_node.greater_child == None:
                    print(f"Node {value_to_find} doesn't exist")
                    return 
                else:
                    current_node = current_node.greater_child
            elif current_node.value > value_to_find:
                if current_node.lesser_child == None:
                    print(f"Node {value_to_find} doesn't exist")
                    return
                else:
                    current_node = current_node.lesser_child
    

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.lesser_child = None
        self.greater_child = None