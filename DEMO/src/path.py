#!/usr/bin/env python
# encoding: utf-8

'''Initialize the file'''

import os

PATHDIR = "../"

class InitPath(object):
    '''Initialize the file'''


    def __init__(self, dirname, filename):
        '''Initialize the object'''

        self.dirname = dirname
        self.filename = filename

        if(self.isdir()):
            self.path = self.make_dir()
        else:
            self.path = ''      #若用户给的路径不存在，则将路径设为空


    def show_path(self):
        '''Show the full path'''

        print self.path

    def get_path(self):
        '''return the path'''

        return self.path


    def isdir(self):
        '''Judge users transfer working directory exists'''

        dirc = PATHDIR + self.dirname
        if(os.path.exists(dirc)):
            return True
        return False


    def make_dir(self):
        '''Specify the working directory and file name'''

        dirc = PATHDIR + self.dirname + self.filename
        return dirc

'''
if __name__ == "__main__":
    PATH = InitPath('log/', 'log')
    PATH.show_path()
'''

