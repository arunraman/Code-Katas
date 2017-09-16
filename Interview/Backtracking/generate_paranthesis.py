class Solution():
    def generateParenthesis(self, n):
        result = []
        self.generateparenthesisRecursive(result, "", n , n)
        print result

    def generateparenthesisRecursive(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
            return result
        if left > 0:
            self.generateparenthesisRecursive(result, current + "(", left - 1, right)
        if left < right:
            self.generateparenthesisRecursive(result, current + ")", left, right - 1)

S = Solution()
S.generateParenthesis(3)