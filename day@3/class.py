#!/usr/bin/env python
# encoding: utf-8

#创建一个类
'''
class Employee:
    "所有员工的基类"


    empCount = 0;

    def __init__(self, name, weight):
        self.name = name ;
        self.weight = weight;
        Employee.empCount += 1;

    def displayEmpCount(self):
        print "total Employee.empCount = %d" % Employee.empCount;

    def displayEmployee(self):
        print "the weight of %s is %d" %(self.name, self.weight);


"初始化实例"

"创建Employee的第一个对象"
self = Employee ("ningqi", 48);

self.displayEmpCount();
self.displayEmployee();

print "***************************";

"创建Employee的第二个对象"
self1 = Employee ("niuting", 46);

self1.displayEmpCount();
self1.displayEmployee();
'''

#创建一个类
'''
#FileName: class.py
class Person:
    pass ;

p = Person();
print p;
'''

#使用对象的方法
'''
#FileName: class.py
class Person:
    def sayHi(self):
        print "Hi************\n"

p = Person()
p.sayHi()
'''

#__init__方法
'''
#FileName: class.py
class Person:

    def __init__(self, name):
        self.name = name;
    def sayHi(self):
        print "hello my name is %s " % self.name;

p = Person("ningqi");
p.sayHi();
'''

#使用类与对象

#FileName: class.py
class Person:
    population = 0;

    def __init__(self, name):
        self.name = name;
        print '(Initializing %s)' % self.name;
        Person.population += 1;

    def __del__(self):
        '''I am dying'''
        print '%s say bye' % self.name;

        Person.population -= 1;
        if Person.population == 0:
            print "I am the last one\n";
        else:
            print "there are still %d person left" % Person.population;

    def sayHi(self):
        print "Hi I am %s" %self.name;

    def howMany(self):
        if Person.population == 1:
            print "I am the onely person in here";
        else:
            print "We have %d person in here" % Person.population;

ningqi = Person('ningqi');
ningqi.sayHi();
ningqi.howMany();

niuting = Person('niuting');
niuting.sayHi();
niuting.howMany();

del ningqi;
del niuting;


