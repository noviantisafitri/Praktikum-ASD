class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_item

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def size(self):
        return self.size

# Contoh Penggunaan
queue = QueueLinkedList()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front element:", queue.peek())  # Output: 1
print("Size of queue:", queue.size)  # Output: 3

dequeued_item = queue.dequeue()
print("Dequeued element:", dequeued_item)  # Output: 1

print("Is queue empty?", queue.is_empty())  # Output: False






















