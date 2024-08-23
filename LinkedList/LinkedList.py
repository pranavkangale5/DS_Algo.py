class Node:  # creates a new node
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkeList:
    def __init__(self, value):
        new_node = Node(value)  # calls the Node Class and passes the value
        self.head = new_node
        self.tail = new_node
        self.length = new_node


my_Linkedlist = LinkeList(4)

print(my_Linkedlist.head.value)
