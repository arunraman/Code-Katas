from ListNode import *

class Solution(object):
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        l1, l2  = self.dividelist(head)
        l1 = self.mergeSort(l1)
        l2 = self.mergeSort(l2)
        head = self.mergeLists(l1, l2)
        return head

    def dividelist(self, head):
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        return head, mid

    def mergeLists(self, l1, l2):
        temp = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            temp = l1
            temp.next = self.mergeLists(l1.next, l2)
        else:
            temp = l2
            temp.next = self.mergeLists(l1, l2.next)
        return temp

list1 = LinkedList()                    # Creating a linked list
list1.append(20)                        # Assigning values to linked list in unsorted manner
list1.append(10)
list1.append(50)
list1.append(40)
list1.append(30)

print "Linked list before sorting"
print list1                       # Printing the unsorted linked list

S = Solution()
list1.head = S.mergeSort(list1.head)      # Applying mergeSort to linked list

print "Linked list after sorting"
print list1