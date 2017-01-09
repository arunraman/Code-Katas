import re


def findSubstringinorder(S, L):
    substring = ''.join(str for str in L)
    return [(m.start(), m.end()) for m in re.finditer(substring, S)]


def findSubstringanyorder(S, L):
    n, m, w = len(S), len(L), len(L[0])
    result = []
    for index in xrange(n-m*w+1):
        seg = [S[i:i+w] for i in xrange(index, index+m*w, w)]
        for item in L:
            if item in seg:
                seg.remove(item)
            else:
                break
        if seg == []:
            result.append((index, index+m*w))
    return result

S = "barfoobar"
L = ["foo", "bar", ]
print findSubstringinorder(S, L)
print findSubstringanyorder(S, L)
