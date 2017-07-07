# Question:
# Given two strings, one smaller string (needle) and one bigger string (haystack),
# find all permutations of the shorter string within the longer one.

# For example:
# (needle, haystack) => output
# ('abc', 'abc') => ['abc']
# ('abc', 'cab') => ['cab']
# ('abc', 'cabbac') => ['cab', 'bac']
# ('abcd', 'cab') => []
# ('sis', 'mississippi') => ['iss', 'ssi', 'sis', 'iss', 'ssi']
# ('sis', 'missoissippi') => ['iss', 'iss', 'ssi']


# Length of the Needle = n
# Length of the Haystack = m
# O(n) * O(m)
# {a : 1}

from collections import Counter


def needle_in_haystack(haystack, needle):
    if len(needle) > len(haystack):
        return []
    needle_count = Counter(needle)
    window = len(needle)
    curr_start = 0
    result = []
    while (window <= len(haystack)):
        segment = haystack[curr_start:window]
        if check_segment(segment, needle_count):
            result.append(segment)
        window += 1
        curr_start += 1
    return result


def check_segment(segment, needle_count):
    C = Counter(segment)
    for k, v in needle_count.iteritems():
        if C[k] != v:
            return False
    return True


print needle_in_haystack('abc', 'abc')
print needle_in_haystack('cab', 'abc') # => ['cab']
print needle_in_haystack('cabbac', 'abc')# => ['cab', 'bac']
print needle_in_haystack('cab', 'abcd')# => []
print needle_in_haystack('mississippi', 'sis')# => ['iss', 'ssi', 'sis', 'iss', 'ssi']
print needle_in_haystack('missoissippi', 'sis')# => ['iss', 'iss', 'ssi']


