#!/usr/bin/env python
# encoding: utf-8

'''Configuration log file'''

import logging

class LogConfig(object):
    '''Configuration log file'''

    def __init__(self, path):
        '''Initialize the configuration file'''

        print path
        self.logfile = path
        self.format = '%(levelname)s: %(asctime)s %(filename)s \
%(funcName)s[line:%(lineno)d] %(message)s'
        self.datefmt = '%a, %d %b %Y %H:%M:%S'

    def config_log(self):
        '''config log attribute'''

        logging.basicConfig(filename=self.logfile,
                            filemode='a',
                            level=logging.DEBUG,
                            format=self.format,
                            datefmt=self.datefmt)

    def logger(self):
        '''user logger'''

        logger = logging.getLogger()
        return logger


