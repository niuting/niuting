#!/usr/bin/env python
# encoding: utf-8

#try-except
'''
try:
    fh = open("./tmp.txt", "r+");
    fh.write("this is my tmp file for exception handling!");
    fh.close();
except IOError:
    print "Error: cant find file or write to file\n" ;
else:
    print "Written content in the file successfully\n"
    fh.close();
'''

#try-finally
'''
try:
    fh = open("./tmp.txt", "r");
    fh.write("this is my tmp file for exception handling!");
finally:
    fh.close();
    print "finally";
'''

#try-exception = try-finally
'''
try:
    fh = open("./tmp.txt", "r");
    try:
        fh.write("this is my tmp file for exception handling!");
    except IOError:
        print "Error: cant write to file\n" ;
        fh.close();
    else:
        fh.close();
except IOError:
     print "Error: cant find this file\n" ;
'''

#异常参数
def temp_convert(var):
    try:
        return int(var);
    except ValueError, Argument:
        print "the argument dosen't contain numbers\n", Argument;
    else:
        print "convert sucessfully!\n";

temp_convert('a1s');

