import string
import random


dic_list = [ch for ch in string.ascii_lowercase]
random.shuffle(dic_list)
alphabet = ['r', 'f', 'c', 'g', 'o', 'h', 'p', 'u', 'v', 't', 'd', 'l', 'i',
            'a', 'x', 'z', 'j', 'n', 'y', 'b', 's', 'k', 'q', 'w', 'm', 'e']
list1 = ['foo', 'goo', 'foo', 'rf', 'fr']
list2 = sorted(list1, key=lambda word: [alphabet.index(c) for c in word.lower()])
print list2
key=lambda word: [alphabet.index(c) for c in word.lower()]
print key('bar')
print sorted([key('d'), key('Roo')])