import hashlib
import os

from . import ModelMixin
from . import db


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    # has relationship with comments
    boke = db.relationship('Boke', backref="user")
    comments = db.relationship('Comment', backref="user")
    replys = db.relationship('Reply', backref="user")
    star = db.relationship('Star', backref='user')

    def __init__(self, form):
        super(User, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def valid_login(self, u):
        if u is not None:
            username_equals = u.username == self.username
            password_equals = u.password == self.password
            valid_username_len = len(self.username) >= 3
            valid_password_len = len(self.password) >= 3
            return username_equals and password_equals  and valid_username_len and valid_password_len
        else:
            return False

    # 验证注册用户的合法性的
    def valid(self):
        valid_username = User.query.filter_by(username=self.username).first() == None
        valid_username_len = len(self.username) >= 3
        valid_password_len = len(self.password) >= 3
        # valid_captcha = self.captcha == '3'
        msgs = []
        if not valid_username_len:
            message = '用户名长度必须大于等于 6'
            msgs.append(message)
        elif not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        elif not valid_password_len:
            message = '密码长度必须大于等于 6'
            msgs.append(message)
        # elif not valid_captcha:
        #     message = '验证码必须输入 3'
        #     msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        return status, msgs
    
    def vaild_star_boke(self, id):
        star = self.star
        if len(star) == 0:
            return False
        for i in star:
            if i.boke_id == id:
                return True
        return False


