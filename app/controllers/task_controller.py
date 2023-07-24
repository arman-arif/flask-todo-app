from flask import render_template, request, make_response

from app.db import db
from app.models import Task


class TaskController:
    @staticmethod
    def index():
        tasks = Task.query.all()
        return render_template('index.html', title='Home', tasks=tasks)

    @staticmethod
    def add():
        title = request.form.get('title')
        description = request.form.get('description')
        task = Task.create({
            "title": title,
            "description": description
        })

        return make_response({
            "success": True,
            "data": {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "date_created": task.date_created,
            }
        })

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
