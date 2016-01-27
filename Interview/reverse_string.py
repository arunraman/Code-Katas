#!/usr/bin/python


def reverse_string(string):
    if len(string) == 1:
        return string
    if len(string) < 1:
        return False
    words = string[::-1].split()
    print " ".join([word[::-1] for word in words])


reverse_string("Arun R")
