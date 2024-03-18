class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def size(self):
        return self.size

stack = StackLinkedList()

stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.peek())  # Output: 3
print("Size of stack:", stack.size)  # Output: 3

popped_item = stack.pop()
print("Popped element:", popped_item)  # Output: 3

print("Is stack empty?", stack.is_empty())  # Output: False

