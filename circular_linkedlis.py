class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            
    def display(self):
        if self.head == None:
            print("kosonggg")
        else:
            current = self.head
            while True:
                print(current.data, "====>",end=" ")
                current = current.next
                if current == self.head:
                    break

ll = CircularLinkedList()
ll.add_node(1)  
ll.add_node(2)  
ll.add_node(3) 
ll.display() 
            