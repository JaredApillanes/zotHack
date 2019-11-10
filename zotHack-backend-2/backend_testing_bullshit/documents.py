from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import player

import question_acces

app = Flask(__name__)
api = Api(app)

api.add_resource(Question, '/getquestion')


# api.add_resource(PlayerCreator, '/createplayer')
# api.add_resource(PlayerList, '/player/game/<string:game_id>')
# api.add_resource(Player, '/player/<string:id>')

if __name__ == '__main__':
    from db import mongo
    mongo.init_app(app)
    app.run(port=5000, debug=True)