import datetime
from flask_restful import Resource, reqparse
from bson import json_util
from bson.objectid import ObjectId
from db import mongo

import traceback


class PlayerCreator(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="Name field cannot be left bank!"
                        )

    def post(self):
        # TODO: Implement player creation
        data = PlayerCreator.parser.parse_args()
        '''
        name: data['name']
        game_id: data['game_id]
        points: 0
        '''

        try:
            player_id = mongo.db.players.insert_one({
                "name":data['name'],
                "points": 0
            }).inserted_id
        except:
            return {'message': 'Player can\'t be created'}, 400

        # update your game
        return player_id


class Player(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('answer',
                        type=str,
                        required=True,
                        help="answer field cannot be left blank!"
                        )

    def get(self, id):
        player = mongo.db.players.find_one({"_id": ObjectId(id)})
        if player:
            return json_util._json_convert(player), 200
        return {'message': 'Player not found'}, 404

    def put(self, id, score):
        try:
            player = mongo.db.players.find_one({"_id": ObjectId(id)})
            player.update_one
        except:
            return {'message': 'An error occured trying to look up this Player'}, 500

        if not player:
            return {'message': 'Player not found'}, 404


    def delete(self, id):
        try:
            player = mongo.db.players.find_one({"_id": ObjectId(id)})
        except:
            return {'message': 'An error occured trying to look up this Player'}, 500

        if player:
            try:
                mongo.db.players.delete_one({"_id": ObjectId(id)})
            except:
                return {'message': 'An error occured trying to delete this Player'}, 500
            return {'message': 'Player was deleted'}, 200
        return {'message': 'Player not found'}, 404
