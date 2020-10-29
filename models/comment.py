from . import ModelMixin
from . import db
from . import timestamp


class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    created_time = db.Column(db.Integer, default=0)
    thumbs = db.Column(db.Integer, default=0)
    root_id = db.Column(db.Integer, default=0)
    parent_id = db.Column(db.Integer, default=0)
    # 外键内容
    boke_id = db.Column(db.Integer, db.ForeignKey('bokes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    replys = db.relationship('Reply', backref="comment")

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = timestamp()
