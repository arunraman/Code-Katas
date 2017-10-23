class FenTree (object):

    def __init__(self, array):
        self.array, self.tree = [0] * len(array), [0] * (len(array) + 1)
        for i in range(len(array)):
            self.update(i, array[i])

    def get_parent(self, child):
        return (child - (child & -child))

    def get_next(self, index):
        return (index + (index & -index))

    def update(self, index, item):
        current, self.array[index] = self.array[index], item
        item -= current
        index += 1
        while (index <= len(self.array)):
            self.tree[index] += item
            index = self.get_next(index)

    def prefix_sum(self, index):
        index += 1
        total = 0
        while (index > 0):
            total += self.tree[index]
            index = self.get_parent(index)
        return (total)

    def range_sum(self, x, y):
        return (self.prefix_sum(max(x, y)) - self.prefix_sum(min(x, y) - 1))

    def describe(self):
        print ('ARRAY =>\t', self.array)
        print ('Binary Indexed Tree =>\t', self.tree)

if (__name__ == '__main__'):
    tree = FenTree([3, 2, -1, 6, 5, 4])
# tree = FenTree ([int (i) for i in input ('Enter the array
# (space-separated integers): ').split ()]);
    tree.describe()

    tree.update(4, 8)  # replaces 5 with 8 in list given to the fenwick tree
    tree.describe()

    print (tree.range_sum(1, 5))  # returns 2-1+6+5+4
    print (tree.prefix_sum(5))  # returns 3+2-1+6+5+4
