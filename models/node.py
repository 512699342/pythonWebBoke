from . import ModelMixin
from . import db
from . import timestamp


class Node(db.Model, ModelMixin):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500),default='尚未有简述')
    # has relationship with topic
    bokes = db.relationship('Boke', backref="node")


    def __init__(self, form):
        self.name = form.get('name', '')
