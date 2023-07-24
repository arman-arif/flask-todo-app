from datetime import datetime

from app.db import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    done = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id

    @staticmethod
    def create(values: dict):
        new_task = Task(title=values['title'], description=values['description'])
        db.session.add(new_task)
        db.session.commit()

        return new_task
