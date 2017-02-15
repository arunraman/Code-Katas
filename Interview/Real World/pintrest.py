from collections import defaultdict
import re


def sum_aggregation(array, sampling_period):
    dict = defaultdict(list)
    date_dict = {}
    sum = 0
    total = 0
    count = 0
    for i in array:
        key_1 = i[0].split()[0]
        key = i[0].split()[1]
        k = re.split('\:', key)
        if k[0] in dict and key_1 in date_dict:
            dict[k[0]].append(i[1])
            date_dict[key_1] = dict
        elif key_1 not in date_dict:
            dict = defaultdict(list)
            dict[k[0]].append(i[1])
            date_dict[key_1] = dict
        else:
            dict[k[0]].append(i[1])
            date_dict[key_1] = dict

    if sampling_period == "1 Hour":
        for date, samps in date_dict.iteritems():
            for k, v in samps.iteritems():
                if len(v) == 12:
                    for j in v:
                        sum += j
                    avg = sum/12
                    print "Sum Aggregation of " + str(date) + " " + str(k) \
                          + " " + str(sum)
                    print "Avg Aggregation of " + str(date) + " " + str(k) \
                          + " " + str(avg)
                    sum = 0
                else:
                    print "Not enough entries for " + str(k)

    elif sampling_period == "1 Day":
        for date, samps in date_dict.iteritems():
            for k, v in samps.iteritems():
                if len(v) == 12:
                    count += 1
                    for j in v:
                        sum += j
                total += sum
                sum = 0
            day_avg = total / (count * 12)
            print "Sum Aggregation of " + str(date) + " " + str(total)
            print "Avg Aggregation of " + str(date) + " " + str(day_avg)
            total = 0
            day_avg = 0

array = [
    ['2016-07-25 12:00', 398],
    ['2016-07-25 12:05', 350],
    ['2016-07-25 12:10', 390],
    ['2016-07-25 12:15', 387],
    ['2016-07-25 12:20', 401],
    ['2016-07-25 12:25', 403],
    ['2016-07-25 12:30', 406],
    ['2016-07-25 12:35', 430],
    ['2016-07-25 12:40', 410],
    ['2016-07-25 12:45', 415],
    ['2016-07-25 12:50', 420],
    ['2016-07-25 12:55', 402],
    ['2016-07-25 13:00', 405],
    ['2016-07-25 13:05', 421],
    ['2016-07-25 13:10', 431],
    ['2016-07-25 13:15', 421],
    ['2016-07-25 13:20', 416],
    ['2016-07-25 13:25', 443],
    ['2016-07-25 13:30', 437],
    ['2016-07-25 13:35', 425],
    ['2016-07-25 13:40', 414],
    ['2016-07-25 13:45', 419],
    ['2016-07-25 13:50', 439],
    ['2016-07-25 13:55', 420],
    ['2016-07-25 14:00', 410],
    ['2016-07-25 14:05', 399],
    ['2016-07-25 14:10', 390],
    ['2016-07-26 14:10', 390],
]

sum_aggregation(array, "1 Hour")
sum_aggregation(array, "1 Day")
