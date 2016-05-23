from collections import Counter

TRANSITIONS = {
    0: [4, 6],
    1: [8, 6],
    2: [7, 9],
    3: [8, 4],
    4: [9, 3, 0],
    5: [],
    6: [7, 1, 0],
    7: [2, 6],
    8: [3, 1],
    9: [2, 4],
}


def answer(start, end, count):
    level = 1
    nodes = Counter([start])
    while level < count:
        new_nodes = Counter()
        for node, freq in nodes.iteritems():
            for n in TRANSITIONS[node]:
                new_nodes[n] += freq
        level += 1
        nodes = Counter(new_nodes)
    return "{}".format(nodes[end])


if __name__ == '__main__':
    # for i in range(2, 20, 2):
    print answer(6, 2, 101)
    # table()