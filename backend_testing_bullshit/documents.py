from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import player

import json

app = Flask(__name__)
api = Api(app)


def abort_if_todo_doesnt_exist(_id):
    if _id not in ELEMENTS:
        abort(404, message="{} doesn't exist".format(_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

api.add_resource(PlayerCreator, '/createplayer')
api.add_resource(PlayerList, '/player/game/<string:game_id>')
api.add_resource(Player, '/player/<string:id>')

if __name__ == '__main__':
    from db import mongo
    mongo.init_app(app)
    app.run(port=5000, debug=True)