from models import Todo
from flask.json import JSONEncoder, JSONDecoder

class TodoJSONEncoder(JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, Todo):
            return {
                'id': obj.id, 
                'description': obj.description,
                'duedate': obj.duedate,
                'done': obj.done,
                'priority': obj.priority
            }
        return super(TodoJSONEncoder, self).default(obj)


class TodoJSONDecoder(JSONDecoder):
    
    def __init__(self, encoding = "utf-8"):
        JSONDecoder.__init__(self, 
            object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        todo = Todo()
        todo.description = d['description']
        return todo
