def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    result, dvd = "", n

    while dvd:
        result += chr((dvd - 1) % 26 + ord('A'))
        dvd = (dvd - 1) / 26

    return result[::-1]

for i in xrange(29):
    print convertToTitle(i)