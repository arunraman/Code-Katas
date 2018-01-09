class p020(object):
    def validParentheses(self, expr):
        opening = set('([{')
        closing = set(')]}')
        match = {('(', ')'), ('[', ']'), ('{', '}')}
        stack = []
        for char in expr:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if len(stack) == 0:
                    return False
                lastopen = stack.pop()
                if (lastopen, char) not in match:
                    return False
        return len(stack) == 0
