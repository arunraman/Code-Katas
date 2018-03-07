
def largestNumber(num):
    num = [str(x) for x in num]
    num.sort(cmp=lambda x, y: cmp(y + x, x + y))
    return ''.join(num) or '0'

arr = [3, 30, 34, 5, 9]
print largestNumber(arr)
