coins = [1, 5, 10, 25]


def num_coins(target_sum):
    if target_sum is None or target_sum < 1:
        return False

    path = []
    inspect(target_sum, path, [])
    return len(path)


def inspect(target_sum, paths, current_path):
    if target_sum == 0:
        path = sorted(paths)
        if path not in paths:
            paths.append(path)
            return

    for coin in coins:
        if coin <= target_sum:
            current_path.append(coin)
            inspect(target_sum - coin, paths, current_path)
            current_path.remove(coin)
    return

print num_coins(5)
