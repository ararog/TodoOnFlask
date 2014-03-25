from utils import TodoJSONEncoder, TodoJSONDecoder
from todo import app, db
from models import Todo
from flask import request, Response, json

@app.route('/')
def index():
    todos = Todo.query.order_by(Todo.description).all()
    return json.dumps(todos, cls = TodoJSONEncoder)

@app.route('/<int:task_id>', methods=['GET'])
def show(task_id):
    todo = Todo.query.get(task_id)
    return json.dumps(todo, cls = TodoJSONEncoder)

@app.route('/', methods=['POST'])
def create():
    todo = json.loads(request.data, cls = TodoJSONDecoder)
    db.session.add(todo)
    db.session.commit()

    return json.dumps(todo, cls = TodoJSONEncoder)

@app.route('/<int:task_id>', methods=['PUT'])
def update(task_id):
    remote_todo = json.loads(request.data, cls = TodoJSONDecoder)

    todo = Todo.query.get(task_id)
    todo.description = remote_todo.description
    db.session.commit()

    todos = Todo.query.order_by(Todo.description).all()
    return json.dumps(todos, cls = TodoJSONEncoder)

@app.route('/<int:task_id>', methods=['DELETE'])
def destroy(task_id):
    todo = Todo.query.get(task_id)
    db.session.delete(todo)
    db.session.commit()
    todos = Todo.query.order_by(Todo.description).all()
    return json.dumps(todos, cls = TodoJSONEncoder)
