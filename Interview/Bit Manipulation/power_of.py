def power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def power_of_four(n):
    return n > 0 and (n & (n - 1)) == 0 and ((n & 1431655765) == n)


print power_of_two(1024)
print power_of_four(16)