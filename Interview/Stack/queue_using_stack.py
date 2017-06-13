class Queue(object):
    def __init__(self, size):
        """
        initialize your data structure here.
        """
        self.capacity = size
        self.inStack, self.outStack = [], []
        self.queueLength = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.queueLength < self.capacity:
            self.inStack.append(x)
            self.queueLength += 1
        else:
            print "Queue Full"
        #print self.inStack

    def pop(self):
        """
        :rtype: nothing
        """
        if self.queueLength != 0 and self.queueLength <= self.capacity:
            self.move()
            self.outStack.pop()
            self.queueLength -= 1
        else:
            print "Queue is empty"

    def peek(self):
        """
        :rtype: int
        """
        if self.queueLength != 0:
            self.move()
            return self.outStack[-1]
        else:
            return "Queue is empty"


    def empty(self):
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack)

    def move(self):
        """
        :rtype nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

q = Queue(2)
q.push(1)
#print q.peek()
q.push(2)
q.push(3)
#q.push(4)
print q.peek()
q.pop()
print q.peek()
q.pop()
print q.peek()
#q.push(4)
#print q.pop()