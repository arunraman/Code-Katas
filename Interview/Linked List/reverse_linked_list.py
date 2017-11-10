def reverseList(self, head):
    dummy = ListNode(float("-inf"))
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next