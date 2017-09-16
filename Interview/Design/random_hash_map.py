import random


class RandomHash:
    def __init__(self):
        self.M = {}
        self.P = {}
        self.elems = []

    def put(self, k, v):
        if k in self.M:
            self.M[k] = v
        else:
            self.M[k] = v
            self.P[k] = len(self.elems)
            self.elems.append(k)

    def get(self, k):
        if k not in self.M: return None
        return self.M[k]

    def delete(self, k):
        if k not in self.M: return False
        p = self.P[k]
        self.elems[p], self.elems[-1] = self.elems[-1], self.elems[p]
        self.P[self.elems[p]] = p
        del M[k]
        del P[k]
        self.elems.pop()
        return True

    def getRandom(self):
        if not self.elems: return None
        k = self.elems[random.randint(1, len(self.elems)) - 1]
        return k, M[k]
