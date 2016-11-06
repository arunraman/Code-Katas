def twosum(nums=(6, 7, 11, 15, 3, 6, 5, 3), target=6):
    lookup = dict(((v, i) for i, v in enumerate(nums)))
    return next(((i+1, lookup.get(target-v)+1)
                 for i, v in enumerate(nums)
                if lookup.get(target-v, i) != i), None)

twosum()
