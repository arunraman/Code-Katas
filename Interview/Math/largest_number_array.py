
def largestNumber(arr):
    arr = sorted([str(x) for x in arr], cmp=lambda x, y: cmp(y+x, x+y))
    print arr
    ans = ''.join(arr).lstrip('0')
    return ans or '0'

arr = [3, 30, 34, 5, 9]
print largestNumber(arr)
