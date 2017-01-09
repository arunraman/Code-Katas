def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


print list(all_perms([1, 2, 3]))
print list(all_perms("abc"))


def next_highest_permutation(num):
    perms_list = sorted(list(all_perms(num)))
    for i in xrange(len(perms_list)):
        if perms_list[i] == num:
            return perms_list[i + 1]

print next_highest_permutation([1, 2, 3])