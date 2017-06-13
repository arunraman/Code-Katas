class Solution():
    def simplifyPaths(self, path):
        stack = []
        tokens = path.split('/')
        for token in tokens:
            if token == '..' and stack:
                stack.pop()
            elif token != '..' and token != '.' and token:
                stack.append(token)
        return "/" +  "/".join(stack)


S = Solution()

print S.simplifyPaths('/a/./b/../../c/')
print S.simplifyPaths('/../')
print S.simplifyPaths('/home//foo/')