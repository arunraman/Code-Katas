class ListNode(object):
    """docstring for ListNode"""

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))