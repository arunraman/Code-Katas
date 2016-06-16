import heapq

nums = [1, 3, 23, 4, 123, 8, 90, 1, 22, 65]
print heapq.nlargest(3, nums)
print heapq.nsmallest(3, nums)
