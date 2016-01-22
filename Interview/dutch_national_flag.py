#!/usr/bin/python

'''
Separate 1, 2, 0 separately
'''


def dutch_national_flag(array):
    high = len(array) - 1
    i = 0
    p = 0
    while i <= high:
        if array[i] == 0:
            array[i], array[p] = array[p], array[i]
            i += 1
            p += 1
        elif array[i] == 2:
            array[i], array[high] = array[high], array[i]
            high = high - 1
        else:
            i += 1


def Main():
    array = [0, 1, 2, 2, 0, 1]
    dutch_national_flag(array)
    print array

if __name__ == '__main__':
    Main()
