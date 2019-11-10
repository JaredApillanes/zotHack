from flask import Flask, jsonify
from flask_restful import Api
from flask_pymongo import PyMongo

from resources.player import PlayerCreator, PlayerList, Player

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/loQ'
api = Api(app)

api.add_resource(PlayerCreator, '/createplayer')
api.add_resource(PlayerList, '/player/game/<string:game_id>')
api.add_resource(Player, '/player/<string:id>')


if __name__ == '__main__':
    from db import mongo
    mongo.init_app(app)
    app.run(port=5000, debug=True)
