def largest_continuous_sum(arr):
    if len(arr) == 0:
        return
    maxSum = currentSum = arr[0]
    for num in arr[1:]:
        currentSum = max(currentSum + num, num)
        maxSum = max(currentSum, maxSum)
    return maxSum


def Main():
    a = [-5, -2, -3, -3, -5]
    b = [5, 2, -3, -11, 18, 1]
    c = [-4, 4, -3, 3, -2, 2]
    d = [4, 5, -9]
    e = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
    f = [1, 2, 3, 4, 5, -20, 10]
    print largest_continuous_sum(a)
    print largest_continuous_sum(b)
    print largest_continuous_sum(c)
    print largest_continuous_sum(d)
    print largest_continuous_sum(e)
    print largest_continuous_sum(f)


if __name__ == '__main__':
    Main()
