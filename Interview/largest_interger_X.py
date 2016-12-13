# Give n a list of sorted integers, find out largest integer X such that there are at
# atleast X number in the list which are >= X

# [1,2,3,3,5] - > 3

def largest_element(nums):
    for i in xrange(len(nums), 0, -1):
        if i <= sum(j >= i for j in nums):
            return i

print largest_element([1, 2, 3, 3, 5])
print largest_element([1, 4, 4])
print largest_element([1, 3, 4, 4, 4, 5])