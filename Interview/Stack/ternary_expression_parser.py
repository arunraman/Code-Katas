class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return ""

        stack = []
        for c in reversed(expression):
            if stack and stack[-1] == '?':
                stack.pop()  # pop '?'
                first = stack.pop()
                stack.pop()  # pop ':'
                second = stack.pop()

                if c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)

        return str(stack[-1])

S = Solution()
print S.parseTernary("F?1:T?5:4")