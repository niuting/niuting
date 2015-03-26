#!/usr/bin/env python
# encoding: utf-8

for letter in "python":
    if letter == 'h':
        break
    print "current letter is ", letter

var = 10
var1 = 5
while var > 0:
    while var1 > 0:
        print "current var1 is ", var1
        print "current var is ", var
        var1 = var1 - 1
        if var1 < 5:
            print "var < 5"
            break
    var = var - 1


