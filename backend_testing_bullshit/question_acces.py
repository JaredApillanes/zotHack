from flask_restful import Resource, reqparse
from bson import json_util
from bson.objectid import ObjectId
from db import mongo

import datetime
import traceback
import random

class Question(Resource):
    # TODO: Implement get and delete for question
    def get(self, id):
        question = mongo.db.questions.find_one({"_id":ObjectId(id)})
        if question:
            return json_util._json_convert(question), 200
        return {'message': 'Question not found'}, 404

    def delete(self, id):
        questions = mongo.db.questions.find_one({"_id":ObjectId(id)})

        if not questions:
            return {'message':'Question not found'}, 404
        try:
            mongo.db.questions.delete_one({"_id":ObjectId(id)})
        except:
            return {
                'message':'An error occured while deleting'
            }, 500
        return {'message':'Question was deleted'}, 200