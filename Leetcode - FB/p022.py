class p022(object):
    def generateParentheses(self, n):
        result = []
        self.generateparanthesesRecursive(result, "", n, n)
        print result

    def generateparanthesesRecursive(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
            return result
        if left > 0:
            self.generateparanthesesRecursive(result, current + "(", left - 1, right)
        if left < right:
            self.generateparanthesesRecursive(result, current + ")", left, right - 1)


S = p022()
S.generateParentheses(3)
