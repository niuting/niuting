#!/usr/bin/env python
# encoding: utf-8


import sys

def readfile(filename):
    f = file(filename);
    while True:
        line = f.readline();
        if len(line) == 0:
            break;
        print line,
    f.close();

if len(sys.argv) < 2:
    print 'No action specified.';
    sys.exit();
if sys.argv[1].startswith("--"):
    if sys.argv[1][2:] == 'help':
        print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
    --version : Prints the version number
    --help    : Display this help'''
    elif sys.argv[1][2:] == 'version':
        print 'Version 1.2';
    else:
        print "unknow option";
else:
    for filename in sys.argv[1:]:
        readfile(filename);
