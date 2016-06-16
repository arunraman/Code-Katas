def combine(string):
    if string is None or len(string) < 1:
        return False
    do_combine(string, [], len(string), 0, 0)


def do_combine(string, out_string, length, level, start):
    for i in xrange(start, length):
        out_string.append(string[i])
        print "".join(out_string)

        if i < length - 1:
            do_combine(string, out_string, length, level+1, i+1)
        out_string = out_string[:level]


def permutations(string):
    if len(string) <= 1:
        return string
    perms = permutations(string[1:])
    char = string[0]
    result = []
    for perm in perms:
        for i in xrange(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result


def Main():
    combine("abc")
    print permutations("abc")
if __name__ == '__main__':
    Main()
