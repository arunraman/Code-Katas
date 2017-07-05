def insertionSort(array):
    """ insertion sort implementation
    >>> insertionSort([6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 8, 9, 10]
    """
    l = len(array)
    for i in range(l):
        element = array[i]
        j = i
        while j>0 and array[j-1]>element:
            array[j] = array[j-1]
            j -= 1
        array[j] = element
    return array


def quickSort(array):
    """ quicksort implementation in python
    NOTE: This algo uses O(n) extra space
    to compute quicksort.
    >>> quickSort([6, 6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 6, 8, 9, 10]
    """
    if len(array) <= 1:
        return array
    from random import randrange
    pivot = array[randrange(len(array))]
    lesser = quickSort([a for a in array if a<pivot])
    equal = [a for a in array if a==pivot]
    greater = quickSort([a for a in array if a>pivot])
    return lesser + equal + greater


def mergeSort(array):
    """ perform mergesort on a list of numbers
    >>> mergeSort([5, 4, 1, 6, 2, 3, 9, 7])
    [1, 2, 3, 4, 5, 6, 7, 9]
    >>> mergeSort([3, 2, 4, 2, 1])
    [1, 2, 2, 3, 4]
    """
    if len(array) <= 1:
        return array
    middle = len(array)/2
    a1 = mergeSort(array[:middle])
    a2 = mergeSort(array[middle:])
    return merge(a1, a2)


def merge(a1, a2):
    l1 = len(a1)
    l2 = len(a2)
    i, j = 0, 0
    a = []
    while i<l1 and j<l2:
        if a1[i] <= a2[j]:
            a.append(a1[i])
            i += 1
        else:
            a.append(a2[j])
            j += 1
    if i<l1:
        a.extend(a1[i:])
    elif j<l2:
        a.extend(a2[j:])
    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)