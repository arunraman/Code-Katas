class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, new_val):
        new_node= ListNode(new_val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.head.val, repr(self.head.next))