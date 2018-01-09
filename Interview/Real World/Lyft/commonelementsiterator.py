i1 = iter([1, 2, 3, 4, 5, 6, 10])
i2 = iter([2, 3, 10, 11])

# Output
# cei = CommonElementsIterator(i1, i2)
# cei.getNext() -> 2
# cei.getNext() -> 3
# cei.hasNext() -> True
# cei.getNext() -> 10
# cei.hasNext() -> False
# cei.getNext() -> Exception

class CommonElementsIterator():
    def __init__(self, i1, i2):
        self.i1 = i1
        self.i2 = i2

    def getNext(self):
        x = self.i1
        y = self.i2
        x_1 = next(self.i1)
        y_1 = next(self.i2)
        while(x and y):
            if x_1 == y_1:
                iter(x_1)
                try:
                    x_1 = next(x)
                except:
                    x = False
                try:
                    y_1 = next(y)
                except:
                    y = False
            elif x_1 < y_1:
                try:
                    x_1 = next(x)
                except:
                    x = None
            else:
                try:
                    y_1 = next(y)
                except:
                    y = False

cei = CommonElementsIterator(i1, i2)
print cei.getNext()
#cei.hasNext()
#cei.printVale()

# def common_element(l1, l2):
#     for element in l2:
#         if element in l1:
#             print element

# common_element(l1, l2)

# def common_element_1(l1, l2):
#     ptr1 = 0
#     ptr2 = 0
#     while(ptr1 != len(l1) and ptr2 != len(l2)):
#         if l1[ptr1] == l2[ptr2]:
#             print l1[ptr1]
#             ptr1 += 1
#             ptr2 += 1
#         elif l1[ptr1] < l2[ptr2]:
#             ptr1 += 1
#         else:
#             ptr2 += 1

# common_element_1(l1, l2)