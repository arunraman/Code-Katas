# Given two strings. Write a function that will return true if one string is a rotation of the other string.
# e.g. 'bca' and 'cab' are rotations of 'abc' and the function should return true
# 'barbazfoo', 'oobarbazf' and 'rbazfooba' are rotations of 'foobarbaz'
# string1 = "barbazfoo"
# string2 = "foobarbaz"
#
#
def is_rotation(string1, string2):
    if len(string1) == 1 and len(string2) == 1 and string1[0] == string2[0]:
        return True
    if len(string1) != len(string2):
        return False
    lookup = set()
    for i in xrange(len(string1)):
        lookup.add(rotate(string1, i))
    if string2 not in lookup:
        return False
    else:
        return True


def rotate(str, n):
    return str[n:] + str[:n]


# Write a function that will return an array of integers that occur exactly once in a given array of integers.

# Example: input list [-2,-2,1,-2,0,1,5,3], output list [0, 5, 3]

# Follow up: what if the input list is sorted (ascending)? input [-2,-2,-2,0,1,1,3,5]

def findUniqueSorted(array):
    if len(array) <= 1:
        return list
    seen = set()
    dup = set()
    for j in array:
        if j not in seen and j not in dup:
            seen.add(j)
        else:
            dup.add(j)
            if seen: seen.remove(j)
    print list(seen)


from collections import defaultdict


def findUnique(list):
    if len(list) < 1:
        print "List doesn't exist"
        return False
    elif len(list) == 1:
        return list
    else:
        result = []
        dict = defaultdict(int)
        for i in list:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for key, value in dict.iteritems():
            if value == 1:
                result.append(key)
    return result


findUniqueSorted([-2,-2,-2,0,1,1,3,5])
#print findUnique([-2, -2, 1, -2, 0, 1, 5, 3])
string1 = "barbazfoo"
string2 = "foobarbaz"
print is_rotation(string1, string2)