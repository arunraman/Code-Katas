def removeDuplicates(array):
    if not array:
        return 0
    #dup = set()
    seen = set()
    array = [x for x in array if not (x in seen or seen.add(x))]
    print array

    # for x in array:
    #     if x not in dup and x not in seen:
    #         seen.add(x)
    #     else:
    #         dup.add(x)
    #         if seen: seen.remove(x)
    #
    # print list(seen)

def removeElement(array, element):
    if (len(array) == 1 and array[0] == element) or (len(array) < 1):
        return []
    array = [x for x in array if x!= element]

    print array



removeDuplicates([1, 1, 2])
removeElement([1, 2, 3, 4, 5, 2, 2], 2)