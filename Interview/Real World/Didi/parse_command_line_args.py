# example: "myapp --directory ~/src/foo --verbose --level 5 "
# Output {'directory': '~/src/foo', 'verbose': True, 'level': '5'}

class Solution(object):
    def parseArguments(self, strs):
        arugumentDict = {}
        argumentLists = strs.split()
        i = 1
        while (i <= len(argumentLists) - 1):
            if argumentLists[i][2:] not in arugumentDict:
                if i + 1 < len(argumentLists):
                    tempStr = argumentLists[i + 1][:2]
                    if tempStr != '--':
                        arugumentDict[argumentLists[i][2:]] = argumentLists[i + 1]
                        i += 2
                    else:
                        arugumentDict[argumentLists[i][2:]] = True
                        i += 1
            else:
                if i + 1 < len(argumentLists):
                    i += 2
                else:
                    i += 1

        return arugumentDict


S = Solution()
print S.parseArguments('myapp --directory ~/src/foo --verbose --level 5 ')
print S.parseArguments('myapp --verbose --verbose --verbose')
print S.parseArguments('myapp')
print S.parseArguments('myapp --directory ~/src/foo --verbose --directory ~/src/foo --verbose --verbose')


