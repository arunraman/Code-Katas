from ListNode import *

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

l1 = LinkedList()
l1.append(5)
l1.append(10)
l1.append(15)

l2 = LinkedList()
l2.append(10)

S = Solution()
print S.addTwoNumbers(l1.head, l2.head)
