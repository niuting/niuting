#!/usr/bin/env python
# encoding: utf-8

#import eval from json
import json

data = [{'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}]

print 'data ', repr(data)

#简单的json编码和解码
'''
jsonData = json.dumps(data)
decode = json.loads(jsonData)
print 'jsonData', jsonData
print 'decode ', decode

print 'data ', type(data)
print 'jsonData ', type(jsonData)
print 'decode ', type(decode[0])
'''

#dumps的参数使用

def showJson(jsonData, decode):
    print 'jsonData', jsonData
    print 'decode ', decode

def dumpsArgvs(data):
    jsonData = json.dumps(data, sort_keys = True, indent = 4, separators = (',', ':     '))

    return jsonData

def loadsJson(jsonData):
    loadData = json.loads(jsonData)

    return loadData


jsonData = dumpsArgvs(data)
lodata = loadsJson(jsonData)
showJson(jsonData, lodata)




