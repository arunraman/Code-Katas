def isBalanced(expr):
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
            lastOpen = stack.pop()
            if (lastOpen, char) not in match:
                return False
    return len(stack) == 0

print isBalanced("}{")
print isBalanced('[dklf(df(kl))d]{}')
