from ListNode import ListNode


class p025(object):
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r , l
                for _ in xrange(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
print p025().reverseKGroup(head, 2)