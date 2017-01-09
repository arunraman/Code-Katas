from collections import defaultdict
class two_sum_data_structure():

    def __init__(self):
        self.lookup = defaultdict(int)

    def add(self, number):
        self.lookup[number] += 1

    def find(self, value):
        for key in self.lookup:
            target = value - key
            if target in self.lookup and (target != key or self.lookup[key] > 1):
                return True
        return False

ts = two_sum_data_structure()
ts.add(2)
ts.add(7)
ts.add(11)
ts.add(15)
print ts.find(9)