#!/usr/bin/python


def largest_continous_sum(arr):
    if len(arr) == 0:
        return
    maxSum = currentSum = arr[0]
    for num in arr[1:]:
        currentSum = max(currentSum + num, num)
        maxSum = max(currentSum, maxSum)
    return maxSum


def Main():
    a = [1, 2, 3, 4, 5, -20, 10]
    print largest_continous_sum(a)

if __name__ == '__main__':
    Main()
