from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import player

from question_acces import Question

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/'
api = Api(app)

api.add_resource(Question, '/getquestion')


# api.add_resource(PlayerCreator, '/createplayer')
# api.add_resource(PlayerList, '/player/game/<string:game_id>')
# api.add_resource(Player, '/player/<string:id>')

if __name__ == '__main__':
    from db import mongo
    mongo.init_app(app)
    app.run(port=5000, debug=True)