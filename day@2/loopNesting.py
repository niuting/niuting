#!/usr/bin/env python
# encoding: utf-8

i = 2
while i < 100:
    j = 2
    while j <= i/j:
        if i%j == 0:
            break
        j += 1
    if j > i/j:
        print i, "是素数"
    i += 1

