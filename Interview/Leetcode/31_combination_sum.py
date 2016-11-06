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
            target -
            candidates[start])
        intermediate.pop()
        start += 1


print combinationSum([2, 3, 6, 7], 7)
