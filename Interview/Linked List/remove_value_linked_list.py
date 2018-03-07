from ListNode import *

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

list1 = LinkedList()  # Creating a linked list
list1.append(1)  # Assigning values to linked list in unsorted manner
list1.append(6)
list1.append(2)
list1.append(6)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(6)

S = Solution()
S.removeElements(list1.head, 6)
print list1