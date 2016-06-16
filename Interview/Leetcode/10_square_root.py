def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    t = x
    while t * t > x:
        t = int(t / 2.0 + x / (2.0 * t))
    return t

print mySqrt(10)
