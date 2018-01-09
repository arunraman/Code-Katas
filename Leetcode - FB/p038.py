class p038(object):
    def countAndSay(self, n):
        oldStr = '1'
        for i in xrange(1, n):
            tmp = ''
            count = 1
            for j in xrange(1, len(oldStr) + 1):
                if j < len(oldStr) and oldStr[j] == oldStr[j - 1]:
                    count += 1
                else:
                    tmp += str(count) + oldStr[j - 1]
                    count = 1
            oldStr = tmp
        return oldStr


S = p038()
print S.countAndSay(6)
