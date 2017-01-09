from collections import Counter


def sub_array_sum(array, k):
    start_index = -1
    hash_sum = {}
    current_sum = 0
    keys = set()
    best_index_hash = Counter()
    for i in array:
        start_index += 1
        current_sum += i
        if current_sum - k in hash_sum:
            hash_sum[current_sum - k].append(start_index)
            keys.add(current_sum - k)
        else:
            if current_sum == 0:
                best_index_hash[start_index] = [(0, start_index)]
            else:
                hash_sum[current_sum - k] = [start_index]
    if keys:
        for k_1 in keys:
            best_start = hash_sum.get(k_1)[0]
            best_end_list = hash_sum.get(k_1)[1:]
            for best_end in best_end_list:
                if abs(best_start-best_end) in best_index_hash:
                    best_index_hash[
                        abs(best_start-best_end)].append((best_start+1,
                                                          best_end))
                else:
                    best_index_hash[
                        abs(best_start-best_end)] = [(best_start+1, best_end)]

    if best_index_hash:
        (bs, be) = best_index_hash[max(best_index_hash.keys(), key=int)].pop()
        print array[bs:be+1]
    else:
        print "No sub array with sum equal to " + str(k)


def sub_array_sum_1(array, k):
    start_index = -1
    hash = {}
    hash[0] = -1
    best_start = -1
    best_len = 0
    current_sum = 0
    for i in array:
        start_index += 1
        current_sum += i
        if current_sum - k in hash:
            if start_index - hash[current_sum - k] > best_len:
                best_start = hash[current_sum - k] + 1
                best_len = start_index - hash[current_sum - k]
        else:
            hash[current_sum] = start_index

    if best_len > 0:
        print array[best_start:best_start+best_len]
    else:
        print "No subarray found"


def Main():
    a = [6, -2, 8, 5, 4, -9, 8, -2, 1, 2]
    b = [-8, 8]
    c = [7, 8, -1, 1]
    d = [2200, 300, -6, 6, 5, -9, -5, 9]
    e = [-9, -6, 8, 6, -14, 9, 6]
    sub_array_sum_1(a, 1)
    sub_array_sum_1(b, 0)
    sub_array_sum_1(c, 14)
    sub_array_sum_1(d, 1)
    sub_array_sum_1(e, 2)
    sub_array_sum_1(c, 0)

if __name__ == '__main__':
    Main()
