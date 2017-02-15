def combinationSum(candidates, target):
    result = []
    combinationSumRecu(sorted(candidates), result, 0, [], target)
    return result


def combinationSumRecu(candidates, result, start, intermediate, target):
    if target == 0:
        result.append(list(intermediate))
    while start < len(candidates) and candidates[start] <= target:
        intermediate.append(candidates[start])
        combinationSumRecu(
            candidates,
            result,
            start,
            intermediate,
            target - candidates[start])
        intermediate.pop()
        start += 1

def combinationSum2(candidates, target):
    result = []
    combinationSum2Recu(sorted(candidates), result, 0, [], target)
    return result

def combinationSum2Recu(candidates, result, start, intermediate, target):
    if target == 0:
        result.append(list(intermediate))
    prev = 0
    while start < len(candidates) and candidates[start] <= target:
        if prev != candidates[start]:
            intermediate.append(candidates[start])
            combinationSum2Recu(candidates,
                                result,
                                start + 1,
                                intermediate,
                                target - candidates[start])
            intermediate.pop()
            prev = candidates[start]
        start += 1


print combinationSum([2, 3, 6, 7], 7)
print combinationSum2([10,1,2,7,6,1,5], 8)