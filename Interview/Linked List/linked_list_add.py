class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode

    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        l = head
        carry = 0
        while l1 or l2 or carry:
            sum, carry = carry, 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                sum -= 10
            l.next = ListNode(sum)
            l = l.next
        return head.next

l_1 = ListNode(5)
l_2 = ListNode(10)
S = Solution()
S.addTwoNumbers(l_1, l_2)
