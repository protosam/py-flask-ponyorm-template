#!/usr/bin/env python3
from functools import wraps
from flask import request, abort
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        print("JESUS FUCKING CHRIST?")
        if not 'username' in request.headers:
            abort(401)

        username = request.headers['username']

        return f(username, *args, **kws)
    return decorated_function