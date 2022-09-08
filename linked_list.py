class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, value_to_add):
        new_node = Node(value_to_add)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    
    def find_node(self, value_to_find):
        current_node = self.head
        while current_node.next != None:
            if current_node.value == value_to_find:
                return True
            else:
                current_node = current_node.next
        return False