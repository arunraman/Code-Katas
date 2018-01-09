from collections import defaultdict
import re


def anagram(str1, str2):
    str1 = re.findall(r'[A-Za-z0-9]', str1.lower())
    str2 = re.findall(r'[A-Za-z0-9]', str2.lower())
    if str1 is None or str2 is None or \
            len(str1) != len(str2):
        return False
    hash = defaultdict(int)
    for char in str1:
        hash[char] += 1
    for char in str2:
        hash[char] -= 1
        if hash[char] < 0:
            return False
    return True


print anagram('Dog', 'Cat')
print anagram('Pointers', 'Protiens')
print anagram('A decimal point', "I'm a dot in place")


def anagram_group(string_list):
    anagram_map = defaultdict(list)
    result = []
    for s in string_list:
        sorted_str = "".join(sorted(s))
        anagram_map[sorted_str].append(s)
    for anagram in anagram_map.values():
        anagram.sort()
        result.append(anagram)
    return result


print anagram_group(["cat", "dog", "act", "mac", "cam", "Pointers", "Protiens"])
