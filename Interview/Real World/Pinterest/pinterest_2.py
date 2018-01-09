# http error log:
# [2014/09/25 14:41:22] FATAL www.pinteret.com/test 500
# [2014/09/25 14:42:22] FATAL www.pinteret.com/test 500
# [2014/09/25 14:43:22] FATAL www.pinteret.com/test 500
# [2014/09/25 14:43:32] Warning www.pinteret.com/FATAL 500
#
# [TS] FATAL/Warning url return_code
#
# how many FATAL errors per min
# out:
# 14:41 1
# 14:42 1
# 14:43 2

from collections import defaultdict
import os

class Solution(object):

    def __init__(self):
        self.status_dict = defaultdict(dict)

    def _read_lines(self, HTTP):
        for line in HTTP:
            line = line.strip()
            line = line.replace("[", "")
            line = line.replace("]", "")
            if not line:
                continue
            yield line

    def _read_http_error_log(self, http_log_file):
        if os.path.exists(http_log_file):
            with open(http_log_file) as HTTP:
                for line in self._read_lines(HTTP):
                    data = line.split()
                    time = ':'.join(data[1].split(':')[:2])
                    key = data[0] + " " + time
                    if key not in self.status_dict:
                        self.status_dict[key][data[2]] = 0
                    if data[2] not in self.status_dict[key]:
                        self.status_dict[key][data[2]] = 0
                    self.status_dict[key][data[2]] += 1

    def _print_aggregation(self):
        for date , status in self.status_dict.iteritems():
            for state, count in status.iteritems():
                print date, state, count

    def computeAggregation(self, http_log_file):
        self._read_http_error_log(http_log_file)
        self._print_aggregation()


S = Solution()
S.computeAggregation('http_error.log')

