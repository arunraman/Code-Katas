dependenciesMap1 = {"a":["m","n"], "b":[], "c":["m","x","y"], "m":["k","h"], "n":[], "x":["c"], "y":[], "k":[], "h":[]}

input1 = ["a", "b", "c"]
expected1 = ["a","m", "k", "h", "n", "b", "c", "x", "y"]



def getDependencies(inputList, dependenciesMap):
    dic = {}
    result = []
    dfs(inputList, dependenciesMap, dic, result)
    return result


def dfs(inputList, dependenciesMap, dic, result):
    for key in inputList:
        if not key in dic:
            dic[key] = key
            result.append(key)
            dependencies = dependenciesMap[key]
            dfs(dependencies, dependenciesMap, dic, result)

output1 = getDependencies(input1, dependenciesMap1)
if output1 == expected1:
    print "pass"
else:
    print "fail"