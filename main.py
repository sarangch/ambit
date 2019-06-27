from init import *
import json
from datetime import datetime
import time

# method to calculate sentiment for any input conversatino text
@api.route('/sentiment/<text>')
class Sentiment(Resource):
    def get(self, text):
        score = helper.sentiment_score(text)
        return score

# method to calculate sentiment for any input conversatino text
# and store it to the DB
@api.route('/store_sentiment')
class Sentiment(Resource):
    @api.expect(sentiment_req_fields, validate=True)
    def post(self):
        req = api.payload
        uid = req['uid']
        text = req['text']
        score = helper.sentiment_score(text)
        helper.store(uid, text, score, None, None)
        respJson = {"sentiment": score, "topic": None, "accuracy": None}
        return respJson

@api.route('/unhappy')
class UnhappyUsers(Resource):
    @api.expect(unhappy_req_fields, validate=True)
    def post(self):
        req = api.payload
        max = 0.0
        if 'max' in req:
            max = req['max']
        return helper.unhappyUsers(max)


if __name__ == '__main__':
    app.run(host='0.0.0.0')