#!/usr/bin/env python
# encoding: utf-8

import cPickle as p

shoplistfile = 'shoplist.data';

shoplist = ['apple', 'mango', 'carrot'];

f = file(shoplistfile, 'w');
p.dump(shoplist, f);

f.close();

del shoplist;

'''
f = file(shoplistfile, 'r');
while True:
    line = f.readline();
    if line == 0:
        break;
    print line;
f.close;
'''
f = file(shoplistfile);
storedlist = p.load(f);

print storedlist;


