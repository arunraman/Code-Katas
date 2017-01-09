#
# Consider an object that contains a 10 bit integer, and a string.
# Sort a 10 million array of such objects by the integer (dont care for the string sorting)
# where each object is (10bit integer and a string) in place using 0(1) extra memory
# and in O(n) time complexity

# nandhini@docker.com

import random
import string
import sys
import time

sys.setrecursionlimit(10000000)

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2 - time1) * 1000.0)
        return ret
    return wrap


class Solution():

    def __init__(self):
        self.number_of_sequence = 10000000

    @timing
    def generate_random_object(self):
        # sample sequence
        # [{'num': 920, 'string': 'crlvfzqbve'},
        # {'num': 690, 'string': 'zsigbmbqjr'},
        # {'num': 708, 'string': 'fxcsqkpygh'},
        # {'num': 786, 'string': 'vmtcpvjzwh'},
        # {'num': 904, 'string': 'ydowwmsccr'}
        # ....
        # ...
        # ]

        sequence = [
            {'num': random.randint(0, 1023), 'string': ''.join(
                random.choice(string.lowercase)
                for i in xrange(10))}
            for x in xrange(self.number_of_sequence)]
        return sequence

    @timing
    def merge_sort(self, sequence):
        """Sorts the input array of objects using the merge sort algorithm.
        """
        if len(sequence) <= 1:
            return sequence
        mid = len(sequence) // 2
        left = self.merge_sort(sequence[:mid])
        right = self.merge_sort(sequence[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        """Takes two sorted lists and returns a single sorted list by comparing the
        elements one at a time.
        """
        if not left:
            return right
        if not right:
            return left
        if left[0]['num'] < right[0]['num']:
            return [left[0]] + self.merge(left[1:], right)
        return [right[0]] + self.merge(left, right[1:])


S = Solution()
sequence = S.generate_random_object()
S.merge_sort(sequence)
