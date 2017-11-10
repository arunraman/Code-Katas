import sys

class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, max(self.getMax(), x)))

    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMax(self):
        if self.stack:
            return self.stack[-1][1]
        return -1 * sys.maxint


M = MinStack()
M.push(11)
M.push(2)
M.push(10)
print M.getMax()
