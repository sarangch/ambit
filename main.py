from init import *
from helper_methods import *
import json
from datetime import datetime
import time

@api.route('/sentiment/<conv>')
class QuerySessions(Resource):
    def get(self, conv):
        score = sentiment_score(conv)

        return score

if __name__ == '__main__':
    app.run(host='0.0.0.0')