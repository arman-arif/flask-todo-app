from flask import render_template, request, make_response

from app.db import db
from app.models import Task


class TaskController:
    @staticmethod
    def index():
        tasks = Task.get_list()
        return render_template('index.html', title='Home', tasks=tasks)

    @staticmethod
    def list():
        tasks = Task.get_list()
        return render_template('list.html', tasks=tasks)

    @staticmethod
    def add():
        title = request.form.get('title')
        description = request.form.get('description')
        if (title is not None) and (title != ''):
            task = Task.create({
                "title": title,
                "description": description
            })

            return make_response({
                "success": True,
                "data": task.to_dict(),
                "message": "Task created successfully."
            })

        return make_response({
            'success': False,
            'message': "Invalid task data."
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

        return make_response({
            "success": True,
            "message": "Task deleted successfully."
        })
