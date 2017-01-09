from collections import deque


def maxSlidingWindow(nums, k):
    q = deque()
    max_numbers = []

    for i in xrange(k):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)

    for i in xrange(k, len(nums)):
        max_numbers.append(nums[q[0]])

        while q and nums[i] >= nums[q[-1]]:
            q.pop()

        while q and q[0] <= i - k:
            q.popleft()

        q.append(i)

    if q:
        max_numbers.append(nums[q[0]])

    return max_numbers

print maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
