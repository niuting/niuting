#!/usr/bin/env python
# encoding: utf-8

ftchesrom bottle import route, request, run

@route('/upload', method = 'POST')

def do_upload():
    name = request.forms.get('name')
    data = request.files.get('data')
    if name and data.file:
        raw = data.file.read() #当文件很大时，这个操作将十分危险
        filename = data.filename
       # return "Hello {}! You uploaded {} ({} bytes).".format(name, filename, len(raw))                                            return "You missed a field"
        return "hello world"
    return "You missed a field"

run(host = '0.0.0.0', port = 8080)
