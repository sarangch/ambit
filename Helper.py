from random import randint
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tinydb import Query, TinyDB


class Helper:
    def __init__(self, dbPath='db.json'):
        self.path = dbPath
        self.db = TinyDB(dbPath)
        self.analyzer = SentimentIntensityAnalyzer()

    def _scale(self, number):
        if -1 <= number < -0.95:
            res = -1
        elif -0.95 <= number < -0.85:
            res = -0.9
        elif -0.85 <= number < -0.75:
            res = -0.8
        elif -0.75 <= number < -0.65:
            res = -0.7
        elif -0.65 <= number < -0.55:
            res = -0.6
        elif -0.55 <= number < -0.45:
            res = -0.5
        elif -0.45 <= number < -0.35:
            res = -0.4
        elif -0.35 <= number < -0.25:
            res = -0.3
        elif -0.25 <= number < -0.15:
            res = -0.2
        elif -0.15 <= number < -0.05:
            res = -0.1
        elif -0.05 <= number < 0.05:
            res = 0
        elif 0.05 <= number < 0.15:
            res = 0.1
        elif 0.15 <= number < 0.25:
            res = 0.2
        elif 0.25 <= number < 0.35:
            res = 0.3
        elif 0.35 <= number < 0.45:
            res = 0.4
        elif 0.45 <= number < 0.55:
            res = 0.5
        elif 0.55 <= number < 0.65:
            res = 0.6
        elif 0.65 <= number < 0.75:
            res = 0.7
        elif 0.75 <= number < 0.85:
            res = 0.8
        elif 0.85 <= number < 0.95:
            res = 0.9
        elif 0.95 <= number <= 1:
            res = 1
        else:
            raise ValueError("wrong input value")
        return res

    def unhappyUsers(self, scoreLimit=0.0):
        q = Query()
        vals = self.db.search(q.sentiment < scoreLimit)
        return vals

    def store(self, uid, text, sentiment, topic, accuracy):
        self.db.insert({'uid': uid, 'text': text, 'sentiment': sentiment, 'topic': topic, 'accuracy': accuracy})

    def sentiment_score(self, inputStr):
        if inputStr is None:
            return 0
        vs = self.analyzer.polarity_scores(inputStr)
        number = 0.01 * int(100 * float(vs['compound']))
        number_scaled = self._scale(number)
        return number_scaled

