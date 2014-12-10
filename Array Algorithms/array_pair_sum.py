__author__ = 'arunraman'

'''To find two numbers in a array whose sum is equal to the given value K'''

def array_pair_sum(arr,k):
    if len(arr) < 2:
        return
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))

def Main():
    a = [-1,-1,-3,3,4]
    print array_pair_sum(a,0)

if __name__ == '__main__':
    Main()