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
        data = PlayerCreator.parser.parse_args()

        try:
            player_id = mongo.db.players.insert_one({
                "name": data['name'],
                "score": 0,
            }).inserted_id
            player_created = mongo.db.players.find_one(
                {"_id": player_id})
        except:
            return {'message': 'An error occured inserting the Player'}, 500

        return json_util._json_convert(player_created), 201


class Player(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('points',
                        type=int,
                        required=True,
                        help="required: points to add"
                        )

    def get(self, id):
        player = mongo.db.players.find_one({"_id": ObjectId(id)})
        if player:
            return json_util._json_convert(player), 200
        return {'message': 'Player not found'}, 404

    def put(self, id):
        data = Player.parser.parse_args()
        try:
            player = mongo.db.players.find_one({"_id": ObjectId(id)})
        except:
            return {'message': 'An error occured trying to look up this Player'}, 500

        if not player:
            return {'message': 'Player not found'}, 404

        player['score'] += data['points']

        try:
            mongo.db.players.update_one({"_id": ObjectId(id)}, {
                "$set": {"total_score": player['score']}})
        except:
            return {'message': 'An error occured trying to update this Player with the answer'}, 500

        return json_util._json_convert({"points": data['points']}), 200


class PlayerList(Resource):
    def get(self):
        players = mongo.db.players.find()
        if (players):
            return json_util._json_convert(players), 200
