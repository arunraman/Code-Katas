#!/usr/bin/python
from collections import defaultdict


def missing_number(arr1, arr2):
    dict = defaultdict(int)
    for num in arr1:
        dict[num] += 1
    for num in arr2:
        dict[num] += 1
    for num in dict:
        if dict[num] == 1:
            print num


def Main():
    arr1 = [1, 2, 3, 6, 7]
    arr2 = [1, 3, 2, 5, 8]
    missing_number(arr1, arr2)

if __name__ == '__main__':
    Main()
