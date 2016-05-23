from collections import Counter
words = ['why','are','you','not','looking','in','my','eyes', 'why', 'are', 'a']
count = Counter(words)
print count.most_common(3)