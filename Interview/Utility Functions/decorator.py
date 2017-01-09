#!/usr/bin/python


def accept_n_gt_zero(f):
    def f_n_gt_zero(n, *args, **kwargs):
        if n <= 0:
            raise Exception("n must be > 0")
        else:
            return f(n, *args, **kwargs)
    return f_n_gt_zero


@accept_n_gt_zero
def simple_interest(n, p, r):
    return n * p * r / 100


def Main():
    print simple_interest(1, 200, 2)

if __name__ == '__main__':
    Main()
