a = set([1, 2, 3, 4])
b = set([2, 4, 3, 5])


print a ^ b # Symmetric Diff

print a & b # Common Elements

print b < a # subset (order doesnt matter)

print a | b # Union

print a - b # Difference Element in b are removed from a