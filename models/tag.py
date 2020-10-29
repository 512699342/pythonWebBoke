from . import ModelMixin
from . import db
from . import timestamp


class Tag(db.Model, ModelMixin):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # has relationship with topic
    boke_id = db.Column(db.Integer, db.ForeignKey('bokes.id'))

    def __init__(self, form):
        self.name = form.get('name', '未命名')
