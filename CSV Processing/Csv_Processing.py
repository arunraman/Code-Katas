#!/usr/bin/python

__author__ = 'arunraman'

import csv
import os

class csv_processing(object):

    def __init__(self,data):
        self.data = data
        self.option = os.path.splitext(self.data)[0]
        self.csv_data = []
        self.csv_headers = []

    def read_csv(self):
        with open(self.data) as csv_file:
            csv_op = csv.reader(csv_file, delimiter=',')
            self.csv_headers = next(csv_op,None)
            for row in csv_op:
                self.csv_data.append(row)

    def process_csv(self):
        self.read_csv()
        if self.option == "Football":
            team= []
            goal_difference = []
            for row in self.csv_data:
                 team.append(row[self.csv_headers.index('Team')])
                 goal_difference.append(int(row[self.csv_headers.index('Goals')]) - int(row[self.csv_headers.index('Goals Allowed')]))
            print team[goal_difference.index(min(goal_difference))]
        elif self.option == "Weather":
            days = []
            temp_difference = []
            for row in self.csv_data:
                days.append(row[self.csv_headers.index('Day')])
                temp_difference.append(int(row[self.csv_headers.index('MxT')]) - int(row[self.csv_headers.index('MnT')]))
            print days[temp_difference.index(min(temp_difference))]

def Main():
    csv_1 = csv_processing('Football.csv')
    csv_2 = csv_processing('Weather.csv')
    csv_1.process_csv()
    csv_2.process_csv()


if __name__ == '__main__':
    Main()