from . import ModelMixin
from . import db
from . import timestamp


class See(db.Model, ModelMixin):
    __tablename__ = 'sees'
    id = db.Column(db.Integer, primary_key=True)
    boke_id = db.Column(db.Integer, db.ForeignKey('bokes.id'))
    ip = db.Column(db.String(32),default='0.0.0.0')
    created_time = db.Column(db.Integer, default=0)
    

    def __init__(self, book_id, ip):
        self.boke_id = book_id
        self.ip = ip
        self.created_time = timestamp()