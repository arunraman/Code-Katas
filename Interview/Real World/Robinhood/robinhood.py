# Every 2 seconds, print a pair of metric lines with the following formats:

# marketdata.latency <unix_timestamp> <value (in seconds)> type=quote
# marketdata.latency <unix_timestamp> <value (in milliseconds)> type=request

# Sample output:
# marketdata.latency 1493409709 6.143643 type=quote
# marketdata.latency 1493409709 2.336949 type=request

# In the above lines, the <unix_timestamp> is the unix epoch time at which we are printing the lines (e.g. 1493409709).

# In the first line, the <value> refers to the "quote latency", which represents how stale a particular quote is.
# To derive this value, we will hit the API endpoint https://api.robinhood.com/quotes/SPY/
# (you can open this in a browser or curl this endpoint to see the response).
# The response will be a JSON object containing multiple keys,
# one of which is the "updated_at" time string for the quote.
# The quote latency value will be current time minus this "updated_at" time.

# In the second line, the <value> refers to the "request latency",
#  which is simply the amount of time it took for the API request/response cycle to complete.
# To compute this, we can simply store the times from before and after the request is made, and compute the difference.


import time
import json
import requests


class Solution(object):
    def __init__(self, base_url):
        self.base_url = base_url
        self.data_time_pattern = '%Y-%m-%d %H:%M:%S'

    def getQuote(self):
        while True:
            time1 = int(round(time.time()))
            request_latency_time_1 = time1 * 1000
            jsondata = requests.get(self.base_url)
            request_latency_time_2 = int(round(time.time() * 1000))
            request_latency = abs(request_latency_time_2 - request_latency_time_1)
            updated_at = json.dumps(jsondata.json()['updated_at'])
            updated_at_date, updated_at_time = updated_at.split('T')
            new_date = updated_at_date[1:]
            new_time = updated_at_time[:-2]
            new_date_time = new_date + " " + new_time
            updated_in_epoch = int(time.mktime(time.strptime(new_date_time, self.data_time_pattern)))
            quote_latency = abs(int(round(time.time())) - updated_in_epoch)
            print 'marketdata.latency %s %0.3f type=quote' % (str(time1), (quote_latency) / 1000.0)
            print 'marketdata.latency %s %0.3f type=request' % (str(time1), (request_latency) / 10000.0)
            time.sleep(2)


S = Solution('https://api.robinhood.com/quotes/SPY/')
S.getQuote()