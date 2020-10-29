# for decorators
from functools import wraps

from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import abort

import random

from models.user import User


def current_user():
    cookie = request.cookies.get('user_id', None)
    uid = session.get(cookie, None)
    if uid is not None:
        u = User.query.get(uid)
        return u


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        print('login required', current_user())
        u = current_user()
        if u is None:
            abort(404)
        return f(*args, **kwargs)

    return function
