from . import ModelMixin
from . import db
from . import timestamp


class Star(db.Model, ModelMixin):
    __tablename__ = 'stars'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    boke_id = db.Column(db.Integer, db.ForeignKey('bokes.id'))
    flag = db.Column(db.Integer,default=1)

    def __init__(self,uid,bid):
        self.user_id = uid
        self.boke_id = bid
        self.flag = 1

    def json(self):
        d = dict(
            id=self.id,
            user_id=self.user_id,
            boke_id=self.boke_id,
            flag = self.flag,
        )
        return d