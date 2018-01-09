from ListNode import ListNode

class swapNode(object):
    def swapNodes(self, head):
        stack = []
        slowptr = head
        fastptr = head
        temp = head
        while fastptr.next != None and fastptr.next.next != None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
        slowptr_copy = slowptr.next
        slowptr.next = None

        while slowptr_copy != None:
            stack.append(slowptr_copy.val)
            slowptr_copy = slowptr_copy.next

        while len(stack) != 0:
            newNode = ListNode(float("-inf"))
            newNode.val = stack.pop()
            newNode.next = temp.next
            temp.next = newNode
            temp = temp.next.next

        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
print swapNode().swapNodes(head)