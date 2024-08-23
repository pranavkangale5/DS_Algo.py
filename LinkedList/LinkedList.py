
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
        self.length = 1

    def print_ll_List(self):  # method to print the Linked list
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):  # method to append a node to Lniked List
        new_node = Node(value)  # calls the Node Class and passes the value
        if self.length == 0:  # checks if the linked list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # points the next of the last node
            self.tail = new_node  # updates the tail to the new node
        self.length += 1
        return True


my_linked_list = LinkedList(8)
my_linked_list.print_ll_List()
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.print_ll_List()
