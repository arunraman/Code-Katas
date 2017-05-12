def next_greater_element_1(nums):
    stack, res = [], [-1] * len(nums)
    for i in range(len(nums)) * 2:
        while stack and (nums[stack[-1]] < nums[i]):
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res

def next_greater_element_2(findNums, nums):
    return [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]

def next_greater_element_3(n):
        num = str(n)
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                t = list(num[i:])
                for j in range(len(t)-1, 0, -1):
                    if t[j]>t[0]:
                        first = t.pop(j)
                        rest = sorted(t)
                        res = int(num[:i] + first + ''.join(rest))
                        return res if res <= (2**31-1) else -1
                #print t
                #raise ValueError('Error: cannot find bigger value!')
        return -1

print next_greater_element_1([40,50,11,32,55,68,75])

print next_greater_element_2([4,1,2], [1,3,4,2])

print next_greater_element_3(12)