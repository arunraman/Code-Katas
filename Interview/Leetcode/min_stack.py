class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack_1.append(x)
        if len(self.stack_2) == 0 or x <= self.stack_2[-1]:
            self.stack_2.append(x)
        print self.stack_1, self.stack_2

    def pop(self):
        """
        :rtype: nothing
        """
        top = self.stack_1[-1]
        self.stack_1.pop()
        if top == self.stack_2[-1]:
            self.stack_2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack_1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_2[-1]

S = MinStack()
S.push(10)
S.push(2)
S.push(3)
S.push(1)
S.push(6)
S.push(5)
print S.top()
print S.getMin()
