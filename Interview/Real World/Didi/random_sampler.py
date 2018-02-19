import random

def random_sampling(k, nums):
    '''
    reservoir sampling
    '''
    n = len(nums)
    sample = []
    for i in xrange(n):
        if i < k:
            sample.append(nums[i])
        else:
            p = random.randint(0, i)
            if p < k:
                sample[p] = nums[i]
    return sample