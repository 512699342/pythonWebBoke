from . import ModelMixin
from . import db
from . import timestamp


class Reply(db.Model, ModelMixin):
    __tablename__ = 'replys'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    created_time = db.Column(db.Integer, default=0)
    thumbs = db.Column(db.Integer, default=0);
    reply_id = db.Column(db.Integer, default=0);                
    # 外键内容
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = timestamp()
    
    def thumbs_add(self):
        self.thumbs += 1
    
