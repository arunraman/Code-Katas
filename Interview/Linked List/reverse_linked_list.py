from ListNode import *

class Solution(object):
    def reverseList(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

    def reverse_list(self, head):
        new_head = None  # this is where we build the reversed list (reusing the existing nodes)
        while head:
            temp = head  # temp is a reference to a node we're moving from one list to the other
            head = head.next  # the first two assignments pop the node off the front of the list
            temp.next = new_head  # the next two make it the new head of the reversed list
            new_head = temp
        return new_head

S = Solution()
l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)

print S.reverse_list(l1.head)
