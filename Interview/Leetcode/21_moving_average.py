#!/usr/bin/python


def moving_average(arr, N):
    avg = []
    for i, j in enumerate(arr):
        if i >= N-1:
            avg.append(get_sum(arr, i, N) / N)
    print avg


def get_sum(arr, index, N):
    sum = 0
    index_count = 0
    while (index_count != N):
        sum = sum + arr[index]
        index -= 1
        index_count += 1
    return float(sum)


def Main():
    arr = [5, 6, 8]
    N = 2
    moving_average(arr, N)

if __name__ == '__main__':
    Main()
