#!/usr/bin/python


def bin_search(array, key):
	if array is None or len(array) < 1:
		return False
	if key is None:
		return False
	return bin_search_rec(array, key, 0, len(array) - 1)


def bin_search_rec(array, key, start, end):
	mid = (start + end) / 2
	if array[mid] == key:
		return mid
	elif mid == start or mid == end:
		return False
	elif array[mid] < key:
		return bin_search_rec(array, key, mid, end)
	else:
		return bin_search_rec(array, key, start, mid)


def Main():
	array = [1, 2, 3, 4, 5, 11, 23 ,55, 77, 88]
	print bin_search(array, 11)

if __name__ == '__main__':
    Main()