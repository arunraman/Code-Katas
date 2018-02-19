from ListNode import ListNode

class Solution(object):
    def reverseBetween(self, head, m, n):
        if head == None:
            return None
        dummy = ListNode(float("-inf"))
        dummy.next = head
        pre = dummy

        for i in xrange(0, m - 1):
            pre = pre.next

        start = pre.next
        then = start.next

        for i in xrange(0, n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        return dummy.next


S = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print S.reverseBetween(head, 3, 5)