#!/usr/bin/env python
# encoding: utf-8

import bottle

DATA = ""



@bottle.post("/")
def post_index():
    global DATA
    DATA = bottle.request.body


@bottle.get("/")
def get_index():
    return DATA


bottle.run(host="0.0.0.0", port=4586)
