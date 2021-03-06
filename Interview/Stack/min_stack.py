import sys

class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(self.getMin(), x)))

    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return sys.maxint


M = MinStack()
M.push(3)
M.push(2)
M.push(3)
print M.getMin()
