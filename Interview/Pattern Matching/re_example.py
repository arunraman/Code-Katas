#!/usr/local/bin/python

import re
import urllib2

sites = 'google cnn yahoo amazon'.split()

pat = re.compile(r'<title>+.*</title>+', re.I | re.M)

for s in sites:
    print ('Searching for ...' + s)
    try:
        u = urllib2.urlopen('http://' + s + '.com')
    except:
        print "Not able to open URL"
        continue
    text = u.read()
    title = re.findall(pat, str(text))
    print title

