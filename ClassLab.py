class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        popped = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return popped
queue = QueueUsingStacks()    
print(queue)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())