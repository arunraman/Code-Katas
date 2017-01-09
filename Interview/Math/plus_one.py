def plus_one(digits):
    carry = 1
    for i in xrange(len(digits) - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] / 10
        digits[i] %= 10

    if carry:
        digits = [1] + digits

    print digits

plus_one([1, 1])