from collections import defaultdict

class Solution(object):

    def __init__(self):
        self.date_hash = defaultdict(list)
        self.stats_by_hour = defaultdict(dict)
        self.stats_by_day = defaultdict(dict)


    def parse_list(self, nums):
        for i in xrange(len(nums)):
            date, min = nums[i][0].split(':')
            self.date_hash[date].append(nums[i][1])

    def _hour_aggregation(self):
        for k, v in self.date_hash.iteritems():
            temp_sum = 0
            date, hour = k.split(" ")
            temp_sum = sum(i for i in v)
            self.stats_by_hour[date][hour] = temp_sum / 12

    def _day_aggregation(self):
        count = 0
        for k, v in self.stats_by_hour.iteritems():
            temp_sum = 0
            count += 1
            for hour_sum in v.values():
                temp_sum += hour_sum
            self.stats_by_day[k] = temp_sum / 24

    def compute_aggregation(self, nums):
        S.parse_list(nums)
        S._hour_aggregation()
        S._day_aggregation()

    def get_Sampling(self, sampling_period):
        if sampling_period == '1 Day':
            print self.stats_by_day
        else:
            print self.stats_by_hour

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
    ['2016-07-25 14:10', 390],
    ['2016-07-26 14:10', 390]
]

S = Solution()
S.compute_aggregation(array)
S.get_Sampling("1 Hour")
S.get_Sampling("1 Day")