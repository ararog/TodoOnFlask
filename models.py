from todo import db

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column(db.String(60))
    duedate = db.Column(db.Date)
    priority = db.Column(db.Integer)
    done = db.Column(db.Boolean)
