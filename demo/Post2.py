#!/usr/bin/env python
# encoding: utf-8

import urllib
import httplib
import json

test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
#test_data_urlencode = json.dumps(test_data)
#test_data_urlencode = urllib.urlencode(test_data)
test_data_urlencode = urllib.urlencode(test_data)

requrl = 'http://www.ideawu.net/'
print "1.********************************"
headerdata = {'Host':'http://www.ideawu.net/'}

print "conn.********************************"

conn = httplib.HTTPConnection('http://www.ideawu.net', 6389)
print "request.********************************"
conn.request(method = 'POST', url = requrl, body = test_data_urlencode, headers = headerdata)

print "response.********************************"
response = conn.getresponse()
res = response.read()

print res

conn.close()
