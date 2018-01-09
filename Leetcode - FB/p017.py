class p017(object):

    def __init__(self):
        self.lookup = ["", "", "abc", "def", "ghi", "jkl", "mno"
                       "pqrs", "tuv", "wxyz"]

    def letterComibinations(self, digits):
        if not digits:
            return []

        result = [""]

        for digit in reversed(digits):
            choices = self.lookup[int(digit)]
            m, n = len(choices), len(result)
            result += [result[i % n] for i in xrange(n, m * n)]

            for i in xrange(m * n):
                result[i] += choices[i / n]

        return result

S = p017()
print S.letterComibinations("23")
