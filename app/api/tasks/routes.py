from flask import request
from app.misc.models import Task
from app import session
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def create_task():
    title = request.form.get('title')
    text = request.form.get('text')
    if not title:
        return {"msg": "Title is required!"}, 422
    elif not text:
        return {"msg": "Body text is required!"}, 422
    user_uuid = get_jwt_identity()
    new_task = Task(
        user_uuid=user_uuid,
        title=title,
        text=text
    )
    session.add(new_task)
    session.commit()
    return {"msg": f"Task {title} is created!"}


@jwt_required()
def get_task():
    user_uuid = get_jwt_identity()
    offset = request.args.get('offset')
    limit = request.args.get('limit')
    query = session.query(Task).filter(Task.user_uuid == user_uuid).offset(offset).limit(limit)
    tasks = []
    for task in query:
        tasks.append({
            "id": task.id,
            "title": task.title,
            "text": task.text
        })
    return tasks


@jwt_required()
def delete_task():
    task_id = request.form.get('task_id')
    task = session.query(Task).get(task_id)
    if not task:
        return {"msg": "Task not found!"}
    session.delete(task)
    session.commit()
    return {"msg": "Task completed!"}

