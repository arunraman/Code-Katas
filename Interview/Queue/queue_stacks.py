class Queue(object):

    def __init__(self, size):
        self.queue_length = 0
        self.inStack = [None] * size
        self.outStack = []

    def enqueue(self, element):
        if self.queue_length < len(self.inStack) and \
           self.inStack[self.queue_length] is None:
            self.inStack[self.queue_length] = element
            self.queue_length += 1
        else:
            print "Queue is Full!!"

    def dequeue(self):
        if self.queue_length != 0:
            self.outStack = self.inStack[self.queue_length - 1::-1]
            self.outStack.pop(0)
            self.queue_length -= 1
            self.inStack[self.queue_length] = None
            self.outStack = []
            for i in xrange(len(self.outStack)):
                self.inStack[i] = self.outStack.pop()
        else:
            print "Queue already empty"

    def peek(self):
        self.move()
        return self.outStack[-1]


    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())


q = Queue(4)
#q.show_queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
#for i in xrange(2):
#    q.dequeue()
#    q.show_queue()
print q.peek()
