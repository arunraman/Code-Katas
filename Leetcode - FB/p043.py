class p043(object):
    def multiplyStrings(self, num1, num2):
        res = [0] * (len(num1) + len(num2))
        for i, el1 in enumerate(reversed(num1)):
            for j, el2 in enumerate(reversed(num2)):
                res[i + j] += int(el1) * int(el2)
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10
        while len(res) > 1 and res[-1] == 0: res.pop()
        return ''.join(map(str,res[::-1]))

S = p043()
print S.multiplyStrings('12', '12')
