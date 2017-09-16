def isStrobogrammatic(num):
    return all(c + d in '696 00 11 88' for c, d in zip(num, num[::-1]))

def findStrobogrammatic(n):
    evenMidCandidate = ["11","69","88","96", "00"]
    oddMidCandidate = ["0", "1", "8"]
    if n == 1:
        return oddMidCandidate
    if n == 2:
        return evenMidCandidate[:-1]
    if n % 2:
        pre, midCandidate = findStrobogrammatic(n-1), oddMidCandidate
    else:
        pre, midCandidate = findStrobogrammatic(n-2), evenMidCandidate
    premid = (n-1)/2
    return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]

print isStrobogrammatic(str(69))

print findStrobogrammatic(4)