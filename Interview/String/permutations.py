class Solution(object):

    def all_perms(self, elements):
        if len(elements) <= 1:
            yield elements
        else:
            for perm in self.all_perms(elements[1:]):
                for i in range(len(elements)):
                    # nb elements[0:1] works in both string and list contexts
                    yield perm[:i] + elements[0:1] + perm[i:]

    def next_high_permutation(self, num):
        k, l = -1, 0
        for i in xrange(len(num) - 1):
            if num[i] < num[i + 1]:
                k = i
        if k == -1:
            num.reverse()
            return

        for i in xrange(k + 1, len(num)):
            if num[i] > num[k]:
                l = i

        num[k], num[l] = num[l], num[k]
        num[k + 1:] = num[:k:-1]
        return num

    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            ans = [l[:i]+[n]+l[i:]
                   for l in ans
                   for i in xrange((l+[n]).index(n)+1)]
        return ans

    def clever_hack_for_above(self, num):
        import itertools
        # Will give unique permutations
        perms_list = list(k for k, _ in itertools.groupby(sorted(list(self.all_perms(num)))))
        ind = perms_list.index(num)
        if ind != len(perms_list) - 1:
            return perms_list[ind + 1]
        else:
            return None

S = Solution()
print "Permutations of an array: " + str(list(S.all_perms([1, 1, 2])))
# Will work on String too
print "Permutations of string: " + str(list(S.all_perms("abc")))

print "Next high permutation of number: " + str(S.next_high_permutation([5, 1, 5]))

print S.permuteUnique([5, 1, 5])

print S.clever_hack_for_above([5, 1, 5])