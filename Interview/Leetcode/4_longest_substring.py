from collections import defaultdict
from operator import itemgetter
import re


def repeated_characters_string(str):
    if len(str) == 0:
        return False
    dict = defaultdict(int)
    for c in str:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    print max(dict.iteritems(), key=itemgetter(1))


def lengthOfLongestRepeatingSubstring(s):
    matcher = re.compile(r'(.)\1*')
    m = [match.group() for match in matcher.finditer(s)]
    print max(m, key=len)


def lengthOfLongestNonRepeatingSubstring(s):
    ans, start, end = 0, 0, 0
    countDict = defaultdict(int)
    for c in s:
        end += 1
        countDict[c] += 1
        while countDict[s[start]] > 1:
            countDict[s[start]] -= 1
            start += 1
        ans = max(ans, end - start)
    print ans


def lengthOfLongestSubstringKDistinct(s, k):
    longest, start, distinct_count, visited = 0, 0, 0, defaultdict(int)

    if len(set(s)) < k:
        print "Not enough unique Characters"
        return False

    for i, char in enumerate(s):
        if visited[char] == 0:
            distinct_count += 1
        visited[char] += 1

        while distinct_count > k:
            visited[s[start]] -= 1
            if visited[s[start]] == 0:
                distinct_count -= 1
            start += 1

        longest = max(longest, i - start + 1)
    print longest

def substringCount(s, k):
    d = defaultdict(int)
    max_sub_str_len = 0
    for i in xrange(len(s)):
        sub_str = s[i:i + k]
        if len(sub_str) == k:
            if sub_str in d:
                d[sub_str] += 1
                if d[sub_str] > max_sub_str_len:
                    max_sub_str_len = d[sub_str]
            else:
                d[sub_str] = 1
    print max(d.iteritems(), key=itemgetter(1)) ,max_sub_str_len

def Main():
    repeated_characters_string("aacdefaaaabbccc")
    lengthOfLongestNonRepeatingSubstring("aabca")
    lengthOfLongestRepeatingSubstring("aacdefaaaabbccc")
    lengthOfLongestSubstringKDistinct("aabacbebebe", 3)
    substringCount("ABCGRETCABCG", 3)


if __name__ == '__main__':
    Main()
