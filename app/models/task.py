from app.db import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    done = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<Task %r>' % self.id

    # def create(self, item):
    #     db.session.add(item)
