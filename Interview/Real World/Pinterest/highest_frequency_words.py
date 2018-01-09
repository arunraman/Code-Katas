def highFrequency():
    d = {}
    highFreq = 0
    file = ['cat', 'dog', 'act', 'cat']
    for word in file:
        tmp= "".join(sorted(word))
        if tmp not in d:
            d[tmp] = 0
        d[tmp] += 1
        highFreq = max(highFreq, d[tmp])
    print highFreq

highFrequency()