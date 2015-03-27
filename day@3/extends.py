#!/usr/bin/env python
# encoding: utf-8

class SchoolMember:
    '''Represents any school member'''
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        print '(Init SchoolMember: %s)' % self.name;
    def tell(self):
        '''tell me details'''
        print "Name: %s, Age: %d" % (self.name, self.age);

class Teacher(SchoolMember):
    '''Represent a teacher'''
    def __init__(self, name, age, teach):
        SchoolMember.__init__(self, name, age);
        self.teach = teach;
    def tell(self):
        SchoolMember.tell(self);
        print "Teach: %s" % self.teach;

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age);
        self.marks = marks;
    def tell(self):
        SchoolMember.tell(self);
        print "Marks: %d" % self.marks;

t = Teacher("hong", 21, "math");
#t.tell();

s = Student("huang", 20, 65);
#s.tell();

members = [t, s];
for member in members:
    member.tell();

