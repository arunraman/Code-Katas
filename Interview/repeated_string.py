#!/usr/bin/python


def repeated_string(str):
    if len(str) == 0:
        return False
    rep = ''
    count = 0
    max_rep = ''
    maximum = 0
    index = 0
    start = 0
    i = 0
    for c in str:
        if c == rep:
            count += 1
            if count > maximum:
                max_rep = rep
                maximum = count
                index = start
        else:
            start = i
            rep = c
            count = 1
        i += 1
    print max_rep
    print "The maximum repeated string is %s", str[index:index+count+1]


def Main():
    repeated_string("aacdefaaaabbccc")

if __name__ == '__main__':
    Main()