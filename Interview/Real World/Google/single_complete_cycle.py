def is_complete_cycle(array):
    """
    Determine whether a circular array of relative indices is composed of a
    single complete cycle.
    """
    # Start at the first element in the array, and keep jumping through the
    # array until we meet the original element or we have jumped more times
    # than there are elements in the array.
    count = 0
    index = 0
    while ((count == 0) or (index != 0)) and (count <= len(array)):
        count += 1
        index = (index + array[index]) % len(array)

    if count == len(array):
        return True
    else:
        return False

print is_complete_cycle([2, -1, 1, 2, 2])