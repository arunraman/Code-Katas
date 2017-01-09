class Queue(object):

    def __init__(self, size):
        self.queue_length = 0
        self.stack_1 = [None] * size
        self.stack_2 = []

    def enqueue(self, element):
        if self.queue_length < len(self.stack_1) and \
           self.stack_1[self.queue_length] is None:
            self.stack_1[self.queue_length] = element
            self.queue_length += 1
        else:
            print "Queue is Full!!"

    def dequeue(self):
        if self.queue_length != 0:
            self.stack_2 = self.stack_1[self.queue_length - 1::-1]
            self.stack_2.pop()
            self.queue_length -= 1
            self.stack_1[self.queue_length] = None
            self.stack_2 = []
            for i in xrange(len(self.stack_2)):
                self.stack_1[i] = self.stack_2.pop()
        else:
            print "Queue already empty"

    def peek(self):
        if len(self.stack_1) == 0:
            return None
        else:
            return self.stack_1[0]

    def show_queue(self):
        print self.stack_1


q = Queue(4)
q.show_queue()
for i in range(5):
    q.enqueue(i)
    q.show_queue()
for i in xrange(2):
    q.dequeue()
    q.show_queue()
print q.peek()
