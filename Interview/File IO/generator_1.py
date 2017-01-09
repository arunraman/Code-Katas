#!/usr/bin/python
import time
import random


def tail_f(file):
    interval = 1.0
    while True:
        where = file.tell()
        line = file.readline()
        if not line:
            time.sleep(interval)
            file.seek(where)
        else:
            yield line


def yield_send():
    while True:
        val = yield
        yield val * 10


def Main():
    for line in tail_f(open("generator.txt")):
        print line

    g = yield_send()
    g.next()
    g.send(random.randint(1, 10))


if __name__ == '__main__':
    Main()
