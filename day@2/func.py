#!/usr/bin/env python
# encoding: utf-8

'''
def printname(str):
    "printUserName";
    print str;

    return;

printname("niuting");
printname("ningqi");
'''
#传递对象
'''
def changeList(mylist):
    "change the value of mylist";
    mylist.append(['four', 'five']);

    return;

mylist = ['one', 'two', 'three'];
changeList(mylist);
print mylist;

'''
#传递值
'''
def changeValue(value):
    "change the value of number";
    value = 20;
    print value;

    return;

a = 10;
changeValue(a);
print a;
'''

'''
#命名参数
def printInfo(age, name):
    "命名参数";
    print "name = ", name, "age= ", age;

    return;

printInfo(name = "ningqi", age = 10);
'''
'''
#不定长参数
def printInfo(age, *vartuple):
    "不定长参数"
    print "age = ", age;
    print "++++++++++++++++++++++++"
    for var in vartuple:
        print var;
    print "++++++++++++++++++++++++"

    return;

printInfo(10);
printInfo(10, 20);
printInfo(10, 20, 30);
'''

#匿名函数
sum = lambda arg1, arg2: arg1+arg2;

print "the value of total = ", sum(10, 20);
print "the value of total = ", sum(20, 20);

