#!/usr/bin/python
import random
import string


class Person(object):

    def __init__(self, name):
        self.age = 50
        self.name = name


class Carpenter(Person):

    def __init__(self, name, income, company_name):
        super(Carpenter, self).__init__(name)
        self.income = income
        self.carp_dict = {}
        self.forge = Organization(company_name)

    def insert_info(self):
        self.carp_dict[self.name] = self.income

    def print_info(self):
        print self.carp_dict
        print self.forge.name


class Organization(object):

    def __init__(self, company_name):
        self.name = company_name


def Main():
    C = Carpenter("Arun", 500, "Main Line Timber")
    str = ""
    token = str.join(
        random.choice(
            string.ascii_letters +
            string.digits) for i in xrange(10))
    print token
    C.insert_info()
    C.print_info()


if __name__ == '__main__':
    Main()
