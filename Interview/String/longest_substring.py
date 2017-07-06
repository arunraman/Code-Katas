from collections import defaultdict
from operator import itemgetter
import re


def repeated_characters_string(str):
    from collections import Counter
    if len(str) == 0:
        return False
    string_dict = defaultdict(int)
    for c in str:
        if c in string_dict:
            string_dict[c] += 1
        else:
            string_dict[c] = 1
    # Get top 5 max values
    print Counter(string_dict).most_common(5)
    print max(string_dict.iteritems(), key=itemgetter(1))


def lengthOfLongestRepeatingSubstring(s):
    matcher = re.compile(r'(.)\1*')
    m = [match.group() for match in matcher.finditer(s)]
    print max(m, key=len)


def lengthOfLongestNonRepeatingSubstring(s):
    last_occurrence = {}
    longest_len_so_far = 0
    longest_pos_so_far = 0
    curr_starting_pos = 0
    curr_length = 0

    for k, c in enumerate(s):
        l = last_occurrence.get(c, -1)
        # If no repetition within window, no problems.
        if l < curr_starting_pos:
            curr_length += 1
        else:
            # Check if it is the longest so far
            if curr_length > longest_len_so_far:
                longest_pos_so_far = curr_starting_pos
                longest_len_so_far = curr_length
            # Cut the prefix that has repetition
            curr_length -= l - curr_starting_pos
            curr_starting_pos = l + 1
        # In any case, update last_occurrence
        last_occurrence[c] = k

    # Maybe the longest substring is a suffix
    if curr_length > longest_len_so_far:
        longest_pos_so_far = curr_starting_pos
        longest_len_so_far = curr_length

    print s[longest_pos_so_far:longest_pos_so_far + longest_len_so_far]


def lengthOfLongestSubstringKDistinct(s, k):
    longest, start, distinct_count = 0, 0, 0
    visited = defaultdict(int)
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
    print max(d.iteritems(), key=itemgetter(1))

def Main():
    repeated_characters_string("aacdefaaaabbccc")
    lengthOfLongestNonRepeatingSubstring("aabca")
    lengthOfLongestRepeatingSubstring("aacdefaaaabbccc")
    lengthOfLongestSubstringKDistinct("aabacbebebe", 3)
    substringCount("ABCGRETCABCG", 4)


if __name__ == '__main__':
    Main()
