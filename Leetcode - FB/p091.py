class p091(object):
    def numDecodings(self, s):
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w , (d >'0')*w + (9 < int(p+d) < 27), d
        return w

S = p091()
print S.numDecodings('12')