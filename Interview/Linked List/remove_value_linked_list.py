from ListNode import ListNode

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(float("-inf"))
        dummy.next = head
        prev, curr = dummy, dummy.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

head = ListNode(1)
head.next = ListNode(6)
head.next.next = ListNode(2)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next = ListNode(6)

S = Solution()
S.removeElements(head, 6)
print head