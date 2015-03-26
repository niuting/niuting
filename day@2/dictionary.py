#!/usr/bin/env python
# encoding: utf-8
#import dict


dict = {('name'): ['niuting', 'ningqi'], 'weight': 46, 'school': 'youdian'}

for usrinfo in dict:
    print usrinfo, dict[usrinfo]
dict['age'] = 10
for usrinfo in dict:
    print usrinfo, dict[usrinfo]

print "len(dict) = ", len(dict)
print "输出字典可打印的字符串表示：", str(dict)
print "type:返回输入变量的类型 ", type(dict['name'])
del dict['weight']
for usrinfo in dict:
    print usrinfo, dict[usrinfo]
dict1 = dict.copy()
print "dict1 = ", dict1
print dict.keys()
print dict.items()
#dict.clear();
#for usrinfo in dict:
#    print usrinfo, dict[usrinfo]
#del dict
#print dict['name']

#print len(dict)
