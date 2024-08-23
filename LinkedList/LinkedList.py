
# constructor for the LinkedList

class Node:  # creates a new node
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # calls the Node Class and passes the value
        self.head = new_node
        self.tail = new_node
        self.length = new_node

    def print_ll_List(self):  # method to print the Linked list
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(8)
my_linked_list.print_ll_List()
