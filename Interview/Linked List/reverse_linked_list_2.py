from ListNode import *

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


list1 = LinkedList()  # Creating a linked list
list1.append(1)  # Assigning values to linked list in unsorted manner
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(6)
list1.append(7)
list1.append(8)


S = Solution()
print S.reverseBetween(list1.head, 3, 5)