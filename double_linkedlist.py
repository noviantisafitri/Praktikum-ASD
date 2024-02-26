class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display(self):
        if self.head == None:
            print("kosonggg")
        else:
            current = self.head
            while current:
                print(current.data, "======>",end=" ")
                current = current.next

linkedlist = DoubleLinkedList()
linkedlist.add_node(1)
linkedlist.add_node(2)
# linkedlist.add_node(3)
# linkedlist.add_node(4)
linkedlist.display()