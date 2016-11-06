class Queue(object):
    def __init__(self, size):
        self.queue_length = 0
        self.A = [None] * size
        self.B = []

    def queue_push(self, x):
        if self.queue_length < len(self.A) and self.A[self.queue_length] == None :
            self.A[self.queue_length] = x
            self.queue_length += 1
        else:
            print "Queue is Full"

    def queue_pop(self):
        self.check()
        self.B.pop()

    def check(self):
        if not self.B:
            self.B = self.B + [self.A[self.queue_length - 1]]
            self.queue_length -= 1
        return self.B[-1]


    def is_empty(self):
        return self.A and not self.B

    def print_queue(self):
        print self.A


Q = Queue(5)
Q.queue_push(1)
Q.queue_push(1)
Q.queue_pop()
# Q.queue_push(1)
# Q.queue_push(1)
# Q.queue_push(1)
# Q.queue_push(1)
Q.print_queue()