from flask_restful import Resource, reqparse
from bson import json_util
from bson.objectid import ObjectId

import json

import datetime
import traceback
import random

class Question(Resource):
    def __init__(self):
        with open("questions.json", "rb") as read_file:
            self.unlisted_champs = json.load(read_file)

    def get(self):
        selected_champ = random.choice(list(self.unlisted_champs.keys()))
        print(selected_champ)
        return self.unlisted_champs.pop(selected_champ)
        # if question:
        #     return json_util._json_convert(question), 200
        # return {'message': 'Question not found'}, 404
    
    

if __name__ == "__main__":
    c1 = Question()
    print(c1.get())
    print(c1.get())
    print(c1.get())