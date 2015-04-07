#!/usr/bin/env python
# encoding: utf-8

import bottle

fileInfo = ""

@bottle.route('/api', method = 'POST')
def saveFile():
    file_name = bottle.request.forms.get("file_name")
    file_context = bottle.request.forms.get("file_context")
    global fileInfo
    fileInfo = file_name + ":" + file_context
    return file_name + file_context

@bottle.route('/<filename>')
def getHtml(filename):
    return bottle.static_file(filename, root = './views')

bottle.run(host = '172.17.6.223', port = 8080)

print fileInfo
