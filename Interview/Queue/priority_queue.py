import heapq

class priorityQueue(object):
    def __init__(self):
        self.queue = []

    def addtoQueue(self, priority, item):
        heapq.heappush(self.queue, (priority, item))

    def displayQueue(self):
        print self.queue

    def getItem(self):
        next_item = heapq.heappop(self.queue)
        return next_item

PQ = priorityQueue()
PQ.addtoQueue(5, 'arun')
PQ.addtoQueue(2, 'arun')
PQ.addtoQueue(3, 'arun')
PQ.displayQueue()
print PQ.getItem()
PQ.displayQueue()
