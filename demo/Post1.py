#!/usr/bin/env python
# encoding: utf-8

import urllib
import urllib2

test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
test_data_urlencode = urllib.urlencode(test_data)

requre = ''

req = urllib2.Request(url = requre, data = test_data_urlencode)

#print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res
