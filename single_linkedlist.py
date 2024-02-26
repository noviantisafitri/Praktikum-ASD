# Single linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def add_node_from_tail(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def delete_node(self, data):
        if self.head == None:
            return
        else:
            current = self.head
            while current is not None:
                if current.data == data:
                    if current.next is None:
                        current = None
                        return
                    else:
                        current.data = current.next.data
                        current.next = current.next.next
                        return
                current = current.next

    def display(self):
        if self.head == None:
            print("kosonggg")
        else:
            current = self.head
            while current:
                print(current.data, "======>",end=" ")
                current = current.next
           

linkedlist = SingleLinkedList()
linkedlist.add_node(1)
linkedlist.add_node(2)
linkedlist.add_node(3)
linkedlist.add_node_from_tail(4)
linkedlist.add_node(5)
linkedlist.delete_node(2)
linkedlist.display()




