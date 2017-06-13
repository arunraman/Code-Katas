class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in xrange(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data

buf = RingBuffer(4)
for i in xrange(10):
    buf.append(i)
    print buf.get()