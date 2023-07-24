from flask import render_template

from app.db import db
from app.models import Task


class TaskController:
    @staticmethod
    def index():
        tasks = Task.query.all()
        return render_template('index.html', title='Home', tasks=[])

    @staticmethod
    def add(title, description):
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()

    @staticmethod
    def toggle_done(task_id):
        task = Task.query.get(task_id)

        if task:
            task.done = not task.done
            db.session.commit()

    @staticmethod
    def delete(task_id):
        task = Task.query.get(task_id)

        if task:
            db.session.delete(task)
            db.session.commit()
