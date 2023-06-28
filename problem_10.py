class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(item)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.stack1.pop()

    def is_empty(self):
        return len(self.stack1) == 0

    def size(self):
        return len(self.stack1)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Size of the queue:", queue.size())

print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())

print("Size of the queue:", queue.size())

queue.enqueue(40)
queue.enqueue(50)

print("Is the queue empty?", queue.is_empty())

print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())

print("Is the queue empty?", queue.is_empty())