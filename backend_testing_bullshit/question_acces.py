from flask_restful import Resource, reqparse
from bson import json_util
from bson.objectid import ObjectId
from db import mongo

import json

import datetime
import traceback
import random

class Question(Resource):
    def __init__(self):
        with open("questions.json", "r") as read_file:
            self.unlisted_champs = json.load(read_file)

    def get(self):
        champ_num = random.randint(0, len(self.unlisted_champs) - 1)
        champion_question = self.unlisted_champs[champ_num]
        self.unlisted_champs.pop(champ_num)
        return champion_question
        # if question:
        #     return json_util._json_convert(question), 200
        # return {'message': 'Question not found'}, 404
    
    

if __name__ == "__main__":
    c1 = Question()
    print(c1.get())
    print(c1.get())
    print(c1.get())
