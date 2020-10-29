from . import ModelMixin
from . import db
from . import timestamp
from models.see import See


class Boke(db.Model, ModelMixin):
    __tablename__ = 'bokes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(2000))
    created_time = db.Column(db.Integer, default=0)
    # 点赞，收藏，浏览数，评论数，标签，分类
    see_num = db.Column(db.Integer, default=0);
    star_num = db.Column(db.Integer, default=0);
    thumbs = db.Column(db.Integer, default=0);
    # 外键
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # has relationship with comments
    comments = db.relationship('Comment', backref="boke")
    tags = db.relationship('Tag', backref='boke')
    star = db.relationship('Star', backref='boke');
    see = db.relationship('See', backref='boke');

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.created_time = timestamp()

    def see_add(self,ip):
        s = See.query.filter_by(boke_id=self.id, ip=ip).first()
        boke = self
        iv_time = 60
        if s == None:
            s_add = See(boke.id, ip)
            s_add.save()
            boke.see_num += 1
        else:
            if (timestamp() - s.created_time) > iv_time:
                boke.see_num += 1
                s.created_time = timestamp()
                s.save()
