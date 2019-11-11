from flask import Flask, jsonify
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_cors import CORS

from resources.player import PlayerCreator, PlayerList, Player

app = Flask(__name__)
cors = CORS(app, origins='*')
print("Restarted")
app.config['MONGO_URI'] = 'mongodb://localhost:27017/loQ'
api = Api(app)

api.add_resource(PlayerCreator, '/createplayer')
api.add_resource(PlayerList, '/player/list')
api.add_resource(Player, '/player/<string:id>')


if __name__ == '__main__':
    from db import mongo
    mongo.init_app(app)
    app.run(port=5000, debug=True)
