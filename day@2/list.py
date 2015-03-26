#!/usr/bin/env python
# encoding: utf-8

str1 = ['abc', 'cdee', 'gfh']
str2 = ['acd', 'cdee', 'gah']

print "str1: ", str1
print "str2: ", str2
print "cmp: ", cmp(str1, str2)
print "len: ", len(str1)
print "max: ", max(str1)
print "list: ", list(str1)
str3 = str1.append('fds')
print "append: ", str1
print str1.count('abc')
str4 =  str1.extend(str2)
print "extend: ", str1
print str1
str5 = str1.insert(2, '123')
print "insert: ", str1
str6 =  str1.reverse()
print "reverse: ", str1
str7 = str1.sort()
print str1



